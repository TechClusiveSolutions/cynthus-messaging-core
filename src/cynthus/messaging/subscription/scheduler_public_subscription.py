"""Scheduler Public Subscription class for the Cynthus project"""

from cynthus.messaging.subscription.public_subscription import PublicSubscription


class SchedulerPublicSubscription(PublicSubscription):
    """Represents cynthus-scheduler's subscription to cynthus-events-topic."""

    def __init__(self, **kwargs) -> None:
        super().__init__(name='cynthus-scheduler-public-sub', **kwargs)
