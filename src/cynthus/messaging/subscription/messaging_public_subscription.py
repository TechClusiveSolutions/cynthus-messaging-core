"""Messaging Public Subscription class for the Cynthus project"""

from cynthus.messaging.subscription.public_subscription import PublicSubscription


class MessagingPublicSubscription(PublicSubscription):
    """Represents cynthus-messaging's subscription to cynthus-topic-public."""

    def __init__(self, **kwargs) -> None:
        super().__init__(name='cynthus-messaging-public-sub', **kwargs)
