"""Profile Public Subscription class for the Cynthus project"""

from cynthus.messaging.subscription.public_subscription import PublicSubscription


class ProfilePublicSubscription(PublicSubscription):
    """Represents cynthus-profile's subscription to cynthus-topic-public."""

    def __init__(self, **kwargs) -> None:
        super().__init__(name='cynthus-profile-public-sub', **kwargs)
