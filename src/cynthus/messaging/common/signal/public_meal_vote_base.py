"""Public Meal Vote Signal Base class for the Cynthus project"""

from .public_meal_base import PublicMealSignalBase


class PublicMealVoteSignalBase(PublicMealSignalBase, abstract=True):
    """Intermediate base for all public meal vote signals. Sets the aggregate component."""

    aggregate = 'vote'
