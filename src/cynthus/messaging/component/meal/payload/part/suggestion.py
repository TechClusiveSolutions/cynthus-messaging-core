"""Suggestion payload part class for the Cynthus project"""

from pydantic import BaseModel, Field
from uuid import UUID

from .meal import Meal


class MealSuggestion(BaseModel):
    """Represents a meal object in a signal payload"""
        
    id_: UUID = Field(..., alias='id', description='The suggestion identifier')
    name: str = Field(..., description='The meal name')
    meal: Meal = Field(..., description='The meal being suggested')
                