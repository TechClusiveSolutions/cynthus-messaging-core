"""Meal Tag Created signal payload class for the Cynthus project"""

from pydantic import Field

from ....common import SignalPayload


class MealTagCreatedPayload(SignalPayload):
    """Represents the payload part of a meal.tag.created signal message"""

    tag_id: str = Field(..., description='The identifier of the created tag')
    meal_id: str = Field(..., description='The identifier of the meal the tag was applied to')
    tag: str = Field(..., description='The tag value')
