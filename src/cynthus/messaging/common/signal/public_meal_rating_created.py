"""Public Meal Rating Created signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_meal_rating_base import PublicMealRatingSignalBase


class PublicMealRatingCreatedSignal(PublicMealRatingSignalBase):
    """Concrete signal: public.meal.rating.created"""

    action = SignalActionType.CREATED
