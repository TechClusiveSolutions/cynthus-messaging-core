from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from cynthus.messaging.publisher import SignalPublisher
from cynthus.messaging.publisher import signal_publisher as publisher_module


def _client():
    sent = []
    sender = MagicMock()
    sender.send_messages = AsyncMock(side_effect=lambda message: sent.append(message))
    sender.__aenter__ = AsyncMock(return_value=sender)
    sender.__aexit__ = AsyncMock(return_value=False)
    client = MagicMock()
    client.get_topic_sender = MagicMock(return_value=sender)
    client.close = AsyncMock()

    return client, sent


def _message():
    message = MagicMock()
    message.model_dump_json.return_value = '{"event_type": "audit.identity.token.issued"}'
    message.event_type = 'audit.identity.token.issued'
    message.correlation_id = 'corr-1'

    return message


@pytest.mark.asyncio
async def test_a_signal_goes_to_the_events_topic_addressed_by_its_event_type():
    client, sent = _client()

    await SignalPublisher(client).publish(_message())

    client.get_topic_sender.assert_called_once_with(topic_name='cynthus-events-topic')
    assert sent[0].subject == 'audit.identity.token.issued'
    assert sent[0].correlation_id == 'corr-1'
    assert sent[0].application_properties is None


@pytest.mark.asyncio
async def test_the_callers_token_travels_as_a_property_never_in_the_body():
    client, sent = _client()

    await SignalPublisher(client).publish(_message(), access_token='abc.def.ghi')

    assert sent[0].application_properties == {'authorization': 'Bearer abc.def.ghi'}
    assert 'abc.def.ghi' not in str(sent[0])


def test_a_connection_string_selects_the_emulator_client(monkeypatch):
    monkeypatch.setenv('SERVICE_BUS_CONNECTION_STRING', 'Endpoint=sb://x')

    with patch.object(publisher_module, 'ServiceBusClient') as bus:
        publisher = SignalPublisher.from_environment()

    bus.from_connection_string.assert_called_once_with('Endpoint=sb://x')
    assert publisher._client is bus.from_connection_string.return_value
    assert publisher._credential is None


@pytest.mark.asyncio
async def test_without_a_connection_string_the_namespace_and_azure_credentials_are_used(monkeypatch):
    monkeypatch.delenv('SERVICE_BUS_CONNECTION_STRING', raising=False)
    monkeypatch.setenv('SERVICE_BUS_NAMESPACE', 'bus.test.servicebus.windows.net')

    with patch.object(publisher_module, 'ServiceBusClient') as bus, \
            patch.object(publisher_module, 'DefaultAzureCredential') as credential:
        credential.return_value.close = AsyncMock()
        bus.return_value.close = AsyncMock()
        publisher = SignalPublisher.from_environment()

        await publisher.close()

    assert bus.call_args.kwargs == {
        'fully_qualified_namespace': 'bus.test.servicebus.windows.net', 'credential': credential.return_value,
    }
    credential.return_value.close.assert_awaited_once()


@pytest.mark.asyncio
async def test_close_closes_the_client():
    client, _ = _client()

    await SignalPublisher(client).close()

    client.close.assert_awaited_once()


@pytest.mark.asyncio
async def test_one_sender_is_opened_and_reused_for_every_message():
    client, sent = _client()
    publisher = SignalPublisher(client)

    for _ in range(3):
        await publisher.publish(_message())

    assert len(sent) == 3
    client.get_topic_sender.assert_called_once_with(topic_name='cynthus-events-topic')
    client.get_topic_sender.return_value.__aenter__.assert_awaited_once()
    client.get_topic_sender.return_value.__aexit__.assert_not_awaited()


@pytest.mark.asyncio
async def test_messages_published_together_still_share_one_sender():
    import asyncio

    client, sent = _client()
    publisher = SignalPublisher(client)

    await asyncio.gather(*(publisher.publish(_message()) for _ in range(5)))

    assert len(sent) == 5
    client.get_topic_sender.assert_called_once()


@pytest.mark.asyncio
async def test_a_dropped_link_is_replaced_and_the_message_is_sent_again():
    client, sent = _client()
    sender = client.get_topic_sender.return_value
    calls = {'count': 0}

    async def flaky(message):
        calls['count'] += 1

        if calls['count'] == 2:
            raise RuntimeError('link detached')

        sent.append(message)

    sender.send_messages = AsyncMock(side_effect=flaky)
    publisher = SignalPublisher(client)

    await publisher.publish(_message())
    await publisher.publish(_message())

    assert len(sent) == 2
    assert client.get_topic_sender.call_count == 2
    sender.__aexit__.assert_awaited_once()


@pytest.mark.asyncio
async def test_a_failure_on_the_fresh_sender_is_raised():
    client, _ = _client()
    client.get_topic_sender.return_value.send_messages = AsyncMock(side_effect=RuntimeError('bus is down'))

    with pytest.raises(RuntimeError, match='bus is down'):
        await SignalPublisher(client).publish(_message())

    assert client.get_topic_sender.call_count == 2


@pytest.mark.asyncio
async def test_close_closes_the_open_sender_before_the_client():
    client, _ = _client()
    publisher = SignalPublisher(client)
    await publisher.publish(_message())

    await publisher.close()

    client.get_topic_sender.return_value.__aexit__.assert_awaited_once()
    client.close.assert_awaited_once()


@pytest.mark.asyncio
async def test_a_sender_that_will_not_close_does_not_stop_the_close():
    client, _ = _client()
    publisher = SignalPublisher(client)
    await publisher.publish(_message())
    client.get_topic_sender.return_value.__aexit__ = AsyncMock(side_effect=RuntimeError('already closed'))

    await publisher.close()

    client.close.assert_awaited_once()
