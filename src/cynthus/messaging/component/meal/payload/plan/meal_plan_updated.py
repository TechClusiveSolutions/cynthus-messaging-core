"""Meal Plan Updated signal payload class for the Cynthus project"""

from typing import List

from pydantic import Field

from .....common import SignalPayload


class MealPlanUpdatedPayload(SignalPayload):
    """Represents the payload part of a meal.plan.updated signal message"""

    plan_id: str = Field(..., description='The identifier of the modified meal plan')
    updated_fields: List[str] = Field(..., description='The names of the plan attributes that were changed')
