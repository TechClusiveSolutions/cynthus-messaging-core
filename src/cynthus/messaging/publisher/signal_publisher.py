"""Signal publisher for the Cynthus project"""

import asyncio
from os import environ

from azure.identity.aio import DefaultAzureCredential
from azure.servicebus import ServiceBusMessage
from azure.servicebus.aio import ServiceBusClient

from cynthus.core import logging
from cynthus.messaging.topic import CoreSignalTopic

LOGGER = logging.getLogger(__name__)

AUTHORIZATION = 'authorization'
CLIENT_ATTRIBUTE = '_cynthus_signal_publisher'


class SignalPublisher:
    """Publishes `SignalMessage`s to the events topic, the way every service does it.

    One sender is kept open for the publisher's lifetime. Opening and closing a sender costs about a second on every
    message, which would make every acknowledgement slow; sending on an open sender takes tens of milliseconds.
    """

    def __init__(self, client: ServiceBusClient, credential=None) -> None:
        self._client = client
        self._credential = credential
        self._topic = CoreSignalTopic()
        self._sender = None
        self._opening = None

    @classmethod
    def for_client(cls, client: ServiceBusClient) -> 'SignalPublisher':
        """The publisher that belongs to `client`, created the first time it is asked for."""

        # Kept on the client itself: the publisher and the client refer to each other, and both go when the client does
        publisher = vars(client).get(CLIENT_ATTRIBUTE)

        if publisher is None:
            publisher = cls(client)
            setattr(client, CLIENT_ATTRIBUTE, publisher)

        return publisher

    @classmethod
    def from_environment(cls) -> 'SignalPublisher':
        """Uses SERVICE_BUS_CONNECTION_STRING (the emulator) or else SERVICE_BUS_NAMESPACE with Azure credentials."""

        connection_string = environ.get('SERVICE_BUS_CONNECTION_STRING')

        if connection_string:
            return cls(ServiceBusClient.from_connection_string(connection_string))

        credential = DefaultAzureCredential()

        return cls(
            ServiceBusClient(fully_qualified_namespace=environ.get('SERVICE_BUS_NAMESPACE'), credential=credential),
            credential,
        )

    async def publish(self, signal_message, access_token: str | None = None) -> None:
        """`access_token` travels as the `authorization` message property, never in the body (which is logged)."""

        properties = {AUTHORIZATION: f'Bearer {access_token}'} if access_token else None

        def build() -> ServiceBusMessage:
            return ServiceBusMessage(
                body=signal_message.model_dump_json(),
                content_type='application/json',
                subject=signal_message.event_type,
                correlation_id=str(signal_message.correlation_id),
                application_properties=properties,
            )

        try:
            await (await self._open()).send_messages(build())
        except Exception:
            # The link may have been dropped since the last message: start again on a fresh sender, once
            LOGGER.getChild('publish').warning('Sending %s failed; retrying on a new sender', signal_message.event_type)

            await self._discard()

            await (await self._open()).send_messages(build())

    async def close(self) -> None:
        await self._discard()
        await self._client.close()

        if self._credential is not None:
            await self._credential.close()

    def _lock(self) -> asyncio.Lock:
        # Created on first use so the publisher can be built before an event loop is running
        if self._opening is None:
            self._opening = asyncio.Lock()

        return self._opening

    async def _open(self):
        async with self._lock():
            if self._sender is None:
                sender = self._client.get_topic_sender(topic_name=self._topic.name)
                await sender.__aenter__()
                self._sender = sender

            return self._sender

    async def _discard(self) -> None:
        async with self._lock():
            sender, self._sender = self._sender, None

        if sender is not None:
            try:
                await sender.__aexit__(None, None, None)
            except Exception:
                LOGGER.getChild('_discard').debug('The sender was already closed', exc_info=True)
