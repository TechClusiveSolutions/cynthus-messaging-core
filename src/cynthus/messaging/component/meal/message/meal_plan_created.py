"""Meal Plan Created signal message for the Cynthus project"""

from ....common import PublicMealPlanCreatedSignal, SignalMessage

from ..payload import MealPlanCreatedPayload


class MealPlanCreatedMessage(SignalMessage[MealPlanCreatedPayload]):
    """
        Represents a meal plan created signal message

        Emitted by: `cynthus-core-api` when a new meal plan is created for a workspace.
        Functional Purpose: Notifies `cynthus-analysis` and `cynthus-scheduler` of the new plan.
    """

    event_type: str = PublicMealPlanCreatedSignal.name
