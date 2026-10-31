"""Meal Recipes Associated signal payload class for the Cynthus project"""

from typing import List

from pydantic import Field

from ....common import SignalPayload


class MealRecipesAssociatedPayload(SignalPayload):
    """Represents the payload part of a meal.recipes.associated signal message"""

    meal_id: str = Field(..., description='The identifier of the composite meal entry')
    recipe_ids: List[str] = Field(..., description='The identifiers of the recipes linked to the meal entry')
