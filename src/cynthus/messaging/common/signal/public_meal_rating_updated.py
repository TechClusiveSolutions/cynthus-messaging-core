"""Public Meal Rating Updated signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_meal_rating_base import PublicMealRatingSignalBase


class PublicMealRatingUpdatedSignal(PublicMealRatingSignalBase):
    """Concrete signal: public.meal.rating.updated"""

    action = SignalActionType.UPDATED
