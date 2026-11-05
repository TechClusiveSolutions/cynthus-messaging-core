"""Signal publisher for the Cynthus project"""

from os import environ

from azure.identity.aio import DefaultAzureCredential
from azure.servicebus import ServiceBusMessage
from azure.servicebus.aio import ServiceBusClient

from cynthus.messaging.topic import CoreSignalTopic

AUTHORIZATION = 'authorization'


class SignalPublisher:
    """Publishes `SignalMessage`s to the events topic, the way every service does it."""

    def __init__(self, client: ServiceBusClient, credential=None) -> None:
        self._client = client
        self._credential = credential
        self._topic = CoreSignalTopic()

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

        async with self._client.get_topic_sender(topic_name=self._topic.name) as sender:
            await sender.send_messages(
                ServiceBusMessage(
                    body=signal_message.model_dump_json(),
                    content_type='application/json',
                    subject=signal_message.event_type,
                    correlation_id=str(signal_message.correlation_id),
                    application_properties=properties,
                )
            )

    async def close(self) -> None:
        await self._client.close()

        if self._credential is not None:
            await self._credential.close()
