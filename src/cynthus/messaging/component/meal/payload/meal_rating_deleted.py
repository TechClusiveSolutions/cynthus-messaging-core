"""Meal Rating Deleted signal payload class for the Cynthus project"""

from pydantic import Field

from ....common import SignalPayload


class MealRatingDeletedPayload(SignalPayload):
    """Represents the payload part of a meal.rating.deleted signal message"""

    rating_id: str = Field(..., description='The identifier of the removed rating')
    meal_id: str = Field(..., description='The identifier of the meal the rating was removed from')
