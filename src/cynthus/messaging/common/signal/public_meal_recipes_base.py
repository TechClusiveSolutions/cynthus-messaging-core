"""Public Meal Recipes Signal Base class for the Cynthus project"""

from .public_meal_base import PublicMealSignalBase


class PublicMealRecipesSignalBase(PublicMealSignalBase, abstract=True):
    """Intermediate base for all public meal recipes signals. Sets the aggregate component."""

    aggregate = 'recipes'
