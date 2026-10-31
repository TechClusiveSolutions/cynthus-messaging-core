"""Health API Public Subscription class for the Cynthus project"""

from cynthus.messaging.subscription.public_subscription import PublicSubscription


class HealthApiPublicSubscription(PublicSubscription):
    """Represents cynthus-health-api's subscription to cynthus-topic-public."""

    def __init__(self, **kwargs) -> None:
        super().__init__(name='cynthus-health-api-public-sub', **kwargs)
