"""Public Meal Recipes Associated signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_meal_recipes_base import PublicMealRecipesSignalBase


class PublicMealRecipesAssociatedSignal(PublicMealRecipesSignalBase):
    """Concrete signal: public.meal.recipes.associated"""

    action = SignalActionType.ASSOCIATED
