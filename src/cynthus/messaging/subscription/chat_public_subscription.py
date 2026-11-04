"""Chat Public Subscription class for the Cynthus project"""

from cynthus.messaging.subscription.public_subscription import PublicSubscription


class ChatPublicSubscription(PublicSubscription):
    """Represents cynthus-chat's subscription to cynthus-events-topic."""

    def __init__(self, **kwargs) -> None:
        super().__init__(name='cynthus-chat-public-sub', **kwargs)
