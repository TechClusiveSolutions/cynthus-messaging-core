"""Public Subscription base class for the Cynthus project"""

from cynthus.messaging.topic import CoreSignalTopic


class PublicSubscription:
    """
        Represents a service's Azure Service Bus subscription to the core signal topic

        A plain value class: it names the subscription and the topic it belongs to and does not talk to the broker.
        Concrete per-service subscriptions subclass this and supply their own queue name, either as a class attribute
        `name` or through the `name` keyword. Any other keyword arguments are kept in `options`.
    """

    def __init__(self, *, name: str | None = None, **options) -> None:
        name = name if name is not None else getattr(type(self), 'name', None)

        if not isinstance(name, str):
            raise TypeError(f'{type(self).__name__} requires a subscription name')

        self.name = name
        self.topic = CoreSignalTopic()
        self.options = options
