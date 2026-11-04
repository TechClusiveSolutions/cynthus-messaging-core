"""Core Web Signal Subscription class for the Cynthus project"""

from .public_subscription import PublicSubscription


class CoreWebSignalSubscription(PublicSubscription):
    """Represents `cynthus-core-web`'s subscription to `cynthus-events-topic`."""

    name: str = 'cynthus-sub-core-web'
