"""Public Meal Rating Signal Base class for the Cynthus project"""

from .public_meal_base import PublicMealSignalBase


class PublicMealRatingSignalBase(PublicMealSignalBase, abstract=True):
    """Intermediate base for all public meal rating signals. Sets the aggregate component."""

    aggregate = 'rating'
