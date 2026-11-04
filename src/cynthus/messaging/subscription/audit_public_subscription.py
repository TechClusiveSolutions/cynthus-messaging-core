"""Audit Public Subscription class for the Cynthus project"""

from cynthus.messaging.subscription.public_subscription import PublicSubscription


class AuditPublicSubscription(PublicSubscription):
    """Represents cynthus-audit's subscription to cynthus-events-topic."""

    def __init__(self, **kwargs) -> None:
        super().__init__(name='cynthus-audit-public-sub', **kwargs)
