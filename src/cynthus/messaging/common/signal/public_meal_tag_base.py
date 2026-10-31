"""Public Meal Tag Signal Base class for the Cynthus project"""

from .public_meal_base import PublicMealSignalBase


class PublicMealTagSignalBase(PublicMealSignalBase, abstract=True):
    """Intermediate base for all public meal tag signals. Sets the aggregate component."""

    aggregate = 'tag'
