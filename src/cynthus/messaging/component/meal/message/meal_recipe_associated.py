"""Meal Recipes Associated signal message for the Cynthus project"""

from ....common import PublicMealRecipesAssociatedSignal, SignalMessage
from ..payload import MealRecipesAssociatedPayload


class MealRecipesAssociatedMessage(SignalMessage[MealRecipesAssociatedPayload]):
    """
        Represents a meal recipes associated signal message

        Emitted by: `cynthus-core-api` when multiple recipe IDs are linked to a composite meal entry.
        Functional Purpose: Notifies `cynthus-recipe` and `cynthus-analysis` of the new association.
    """

    event_type: str = PublicMealRecipesAssociatedSignal.name
