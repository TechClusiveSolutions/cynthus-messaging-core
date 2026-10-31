"""Core Logistics Signal Subscription class for the Cynthus project"""

from .public_subscription import PublicSubscription


class CoreLogisticsSignalSubscription(PublicSubscription):
    """Represents `cynthus-core-logistics`'s subscription to `cynthus-topic-public`."""

    name: str = 'cynthus-sub-core-logistics'
