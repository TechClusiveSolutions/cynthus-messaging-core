"""Core Inventory Signal Subscription class for the Cynthus project"""

from .public_subscription import PublicSubscription


class CoreInventorySignalSubscription(PublicSubscription):
    """Represents `cynthus-core-inventory`'s subscription to `cynthus-topic-public`."""

    name: str = 'cynthus-sub-core-inventory'
