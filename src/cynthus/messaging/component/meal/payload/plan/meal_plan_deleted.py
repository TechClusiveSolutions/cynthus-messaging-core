"""Meal Plan Deleted signal payload class for the Cynthus project"""

from pydantic import Field

from .....common import SignalPayload


class MealPlanDeletedPayload(SignalPayload):
    """Represents the payload part of a meal.plan.deleted signal message"""

    plan_id: str = Field(..., description='The identifier of the removed meal plan')
