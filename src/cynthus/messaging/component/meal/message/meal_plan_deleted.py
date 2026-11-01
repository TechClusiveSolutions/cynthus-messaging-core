"""Meal Plan Deleted signal message for the Cynthus project"""

from ....common import PublicMealPlanDeletedSignal, SignalMessage
from ..payload import MealPlanDeletedPayload


class MealPlanDeletedMessage(SignalMessage[MealPlanDeletedPayload]):
    """
        Represents a meal plan deleted signal message

        Emitted by: `cynthus-core-api` when a meal plan is removed.
        Functional Purpose: Notifies `cynthus-analysis` and `cynthus-scheduler` to drop the plan from their state.
    """

    event_type: str = PublicMealPlanDeletedSignal.name
