"""Meal Plan Updated signal message for the Cynthus project"""

from ....common import PublicMealPlanUpdatedSignal, SignalMessage

from ..payload import MealPlanUpdatedPayload


class MealPlanUpdatedMessage(SignalMessage[MealPlanUpdatedPayload]):
    """
        Represents a meal plan updated signal message

        Emitted by: `cynthus-core-api` when an existing meal plan is modified.
        Functional Purpose: Notifies `cynthus-analysis` and `cynthus-scheduler` of the change.
    """

    event_type: str = PublicMealPlanUpdatedSignal.name
