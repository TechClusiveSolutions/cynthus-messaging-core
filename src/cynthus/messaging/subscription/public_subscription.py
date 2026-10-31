"""Public Subscription base class for the Cynthus project"""

from faststream.azure import AzureServiceBusSubscription

from cynthus.messaging.topic import CoreSignalTopic


class PublicSubscription(AzureServiceBusSubscription):
    """
        Represents a service's Azure Service Bus subscription to cynthus-topic-public

        Concrete per-service subscriptions should subclass this and supply their own queue name, either as a
        class attribute `name` or through the `name` keyword.
    """

    def __init__(self, *, name: str | None = None, **kwargs) -> None:
        name = name if name is not None else getattr(type(self), 'name', None)

        if not isinstance(name, str):
            raise TypeError(f'{type(self).__name__} requires a subscription name')

        super().__init__(name=name, topic=CoreSignalTopic(), **kwargs)
