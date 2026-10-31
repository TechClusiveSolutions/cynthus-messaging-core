"""Public Meal Rating Deleted signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_meal_rating_base import PublicMealRatingSignalBase


class PublicMealRatingDeletedSignal(PublicMealRatingSignalBase):
    """Concrete signal: public.meal.rating.deleted"""

    action = SignalActionType.DELETED
