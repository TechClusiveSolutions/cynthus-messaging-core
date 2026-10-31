"""Core Cache Public Subscription class for the Cynthus project"""

from cynthus.messaging.subscription.public_subscription import PublicSubscription


class CoreCachePublicSubscription(PublicSubscription):
    """Represents cynthus-core-cache's subscription to cynthus-topic-public."""

    def __init__(self, **kwargs) -> None:
        super().__init__(name='cynthus-core-cache-public-sub', **kwargs)
