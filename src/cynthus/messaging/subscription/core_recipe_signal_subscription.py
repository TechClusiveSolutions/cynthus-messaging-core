"""Core Recipe Signal Subscription class for the Cynthus project"""

from .public_subscription import PublicSubscription


class CoreRecipeSignalSubscription(PublicSubscription):
    """Represents `cynthus-core-recipe`'s subscription to `cynthus-topic-public`."""

    name: str = 'cynthus-sub-core-recipe'
