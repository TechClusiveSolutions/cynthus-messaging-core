"""Core Shopping Signal Subscription class for the Cynthus project"""

from .public_subscription import PublicSubscription


class CoreShoppingSignalSubscription(PublicSubscription):
    """Represents `cynthus-core-shopping`'s subscription to `cynthus-events-topic`."""

    name: str = 'cynthus-sub-core-shopping'
