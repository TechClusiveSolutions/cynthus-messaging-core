"""Core Worker Signal Subscription class for the Cynthus project"""

from .public_subscription import PublicSubscription


class CoreWorkerSignalSubscription(PublicSubscription):
    """Represents `cynthus-core-worker`'s subscription to `cynthus-events-topic`."""

    name: str = 'cynthus-sub-core-worker'
