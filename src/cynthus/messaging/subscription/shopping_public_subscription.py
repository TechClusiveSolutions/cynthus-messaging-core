"""Shopping Public Subscription class for the Cynthus project"""

from cynthus.messaging.subscription.public_subscription import PublicSubscription


class ShoppingPublicSubscription(PublicSubscription):
    """Represents cynthus-shopping's subscription to cynthus-events-topic."""

    def __init__(self, **kwargs) -> None:
        super().__init__(name='cynthus-shopping-public-sub', **kwargs)
