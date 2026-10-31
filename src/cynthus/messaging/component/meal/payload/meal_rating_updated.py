"""Meal Rating Updated signal payload class for the Cynthus project"""

from typing import Optional

from pydantic import Field

from ....common import SignalPayload


class MealRatingUpdatedPayload(SignalPayload):
    """Represents the payload part of a meal.rating.updated signal message"""

    rating_id: str = Field(..., description='The identifier of the updated rating')
    meal_id: str = Field(..., description='The identifier of the meal the rating belongs to')
    score: int = Field(..., description='The revised numeric rating score, e.g. 1–5')
    comment: Optional[str] = Field(None, description='The revised free-text comment; absent if the comment was cleared')
