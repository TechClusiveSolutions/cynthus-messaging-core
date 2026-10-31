"""Identity Public Subscription class for the Cynthus project"""

from cynthus.messaging.subscription.public_subscription import PublicSubscription


class IdentityPublicSubscription(PublicSubscription):
    """Represents cynthus-identity's subscription to cynthus-topic-public."""

    def __init__(self, **kwargs) -> None:
        super().__init__(name='cynthus-identity-public-sub', **kwargs)
