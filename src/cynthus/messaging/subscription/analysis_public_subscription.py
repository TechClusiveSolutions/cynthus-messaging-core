"""Analysis Public Subscription class for the Cynthus project"""

from cynthus.messaging.subscription.public_subscription import PublicSubscription


class AnalysisPublicSubscription(PublicSubscription):
    """Represents cynthus-analysis's subscription to cynthus-topic-public."""

    def __init__(self, **kwargs) -> None:
        super().__init__(name='cynthus-analysis-public-sub', **kwargs)
