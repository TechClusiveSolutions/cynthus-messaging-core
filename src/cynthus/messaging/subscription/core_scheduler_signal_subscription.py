"""Core Scheduler Signal Subscription class for the Cynthus project"""

from .public_subscription import PublicSubscription


class CoreSchedulerSignalSubscription(PublicSubscription):
    """Represents `cynthus-core-scheduler`'s subscription to `cynthus-topic-public`."""

    name: str = 'cynthus-sub-core-scheduler'
