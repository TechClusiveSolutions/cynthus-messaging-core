"""Meal Plan Created signal payload class for the Cynthus project"""

from datetime import datetime

from pydantic import Field

from .....common import SignalPayload


class MealPlanCreatedPayload(SignalPayload):
    """Represents the payload part of a public.meal.plan.created signal message"""

    plan_id: str = Field(..., description='The identifier of the created meal plan')
    horizon: str = Field(..., description='The planning horizon, e.g. week | month')
    start_date: datetime  = Field(..., description='The first date covered by the plan')
    end_date: datetime = Field(..., description='The last date covered by the plan')
    meal_count: int = Field(..., description='The number of meals scheduled within the plan')
    astri_assisted: bool = Field(..., description='Whether Astri assisted in assembling the plan')
