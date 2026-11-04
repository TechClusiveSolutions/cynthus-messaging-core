"""Notification Public Subscription class for the Cynthus project"""

from cynthus.messaging.subscription.public_subscription import PublicSubscription


class NotificationPublicSubscription(PublicSubscription):
    """Represents cynthus-notification's subscription to cynthus-events-topic."""

    def __init__(self, **kwargs) -> None:
        super().__init__(name='cynthus-notification-public-sub', **kwargs)
