"""Meal Rating Created signal payload class for the Cynthus project"""

from typing import Optional

from pydantic import Field

from ....common import SignalPayload


class MealRatingCreatedPayload(SignalPayload):
    """Represents the payload part of a meal.rating.created signal message"""

    rating_id: str = Field(..., description='The identifier of the created rating')
    meal_id: str = Field(..., description='The identifier of the meal that was rated')
    score: int = Field(..., description='The numeric rating score, e.g. 1–5')
    comment: Optional[str] = Field(None, description='An optional free-text comment accompanying the rating')
