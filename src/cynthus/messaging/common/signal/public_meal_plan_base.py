"""Public Meal Plan Signal Base class for the Cynthus project"""

from .public_meal_base import PublicMealSignalBase


class PublicMealPlanSignalBase(PublicMealSignalBase, abstract=True):
    """Intermediate base for all public meal plan signals. Sets the aggregate component."""

    aggregate = 'plan'
