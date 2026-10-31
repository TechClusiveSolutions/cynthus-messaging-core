"""Meal Tag Deleted signal payload class for the Cynthus project"""

from pydantic import Field

from ....common import SignalPayload


class MealTagDeletedPayload(SignalPayload):
    """Represents the payload part of a meal.tag.deleted signal message"""

    tag_id: str = Field(..., description='The identifier of the removed tag')
    meal_id: str = Field(..., description='The identifier of the meal the tag was removed from')
