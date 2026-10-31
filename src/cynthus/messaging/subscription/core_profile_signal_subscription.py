"""Core Profile Signal Subscription class for the Cynthus project"""

from .public_subscription import PublicSubscription


class CoreProfileSignalSubscription(PublicSubscription):
    """Represents `cynthus-core-profile`'s subscription to `cynthus-topic-public`."""

    name: str = 'cynthus-sub-core-profile'
