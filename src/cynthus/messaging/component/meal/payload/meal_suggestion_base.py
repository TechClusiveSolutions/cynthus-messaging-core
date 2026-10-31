"""Meal Suggestion Base message payload class for the Cynthus project"""

from pydantic import Field

from .meal_base import MealPayloadBase
from .part import Meal


class MealSuggestionPayloadBase(MealPayloadBase):
    """Represents the shared part of the payloads of the public.meal.suggestion.* signal messages"""

    meal: Meal
    suggestion_id: str = Field(..., description='The identifier of the suggestion')
