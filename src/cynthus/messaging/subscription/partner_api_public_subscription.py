"""Partner API Public Subscription class for the Cynthus project"""

from cynthus.messaging.subscription.public_subscription import PublicSubscription


class PartnerApiPublicSubscription(PublicSubscription):
    """Represents cynthus-partner-api's subscription to cynthus-topic-public."""

    def __init__(self, **kwargs) -> None:
        super().__init__(name='cynthus-partner-api-public-sub', **kwargs)
