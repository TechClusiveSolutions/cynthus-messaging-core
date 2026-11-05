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
