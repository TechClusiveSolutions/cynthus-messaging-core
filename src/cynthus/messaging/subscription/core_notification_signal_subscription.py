"""Core Notification Signal Subscription class for the Cynthus project"""

from .public_subscription import PublicSubscription


class CoreNotificationSignalSubscription(PublicSubscription):
    """Represents `cynthus-core-notification`'s subscription to `cynthus-topic-public`."""

    name: str = 'cynthus-sub-core-notification'
