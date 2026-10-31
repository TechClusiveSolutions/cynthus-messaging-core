"""Public Meal Tag Created signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_meal_tag_base import PublicMealTagSignalBase


class PublicMealTagCreatedSignal(PublicMealTagSignalBase):
    """Concrete signal: public.meal.tag.created"""

    action = SignalActionType.CREATED
