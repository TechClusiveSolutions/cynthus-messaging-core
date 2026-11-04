"""Billing API Public Subscription class for the Cynthus project"""

from cynthus.messaging.subscription.public_subscription import PublicSubscription


class BillingApiPublicSubscription(PublicSubscription):
    """Represents cynthus-billing-api's subscription to cynthus-events-topic."""

    def __init__(self, **kwargs) -> None:
        super().__init__(name='cynthus-billing-api-public-sub', **kwargs)
