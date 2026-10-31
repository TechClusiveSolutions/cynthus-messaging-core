"""Core API Signal Subscription class for the Cynthus project"""

from .public_subscription import PublicSubscription


class CoreAPISignalSubscription(PublicSubscription):
    """Represents `cynthus-core-api`'s subscription to `cynthus-topic-public`."""

    name: str = 'cynthus-sub-core-api'
