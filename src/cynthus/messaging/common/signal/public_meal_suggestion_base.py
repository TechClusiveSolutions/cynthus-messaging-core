"""Public Meal Suggestion Signal Base class for the Cynthus project"""

from .public_meal_base import PublicMealSignalBase


class PublicMealSuggestionSignalBase(PublicMealSignalBase, abstract=True):
    """Intermediate base for all public meal suggestion signals. Sets the aggregate component."""

    aggregate = 'suggestion'
