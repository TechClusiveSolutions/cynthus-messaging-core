"""Recipe Public Subscription class for the Cynthus project"""

from cynthus.messaging.subscription.public_subscription import PublicSubscription


class RecipePublicSubscription(PublicSubscription):
    """Represents cynthus-recipe's subscription to cynthus-topic-public."""

    def __init__(self, **kwargs) -> None:
        super().__init__(name='cynthus-recipe-public-sub', **kwargs)
