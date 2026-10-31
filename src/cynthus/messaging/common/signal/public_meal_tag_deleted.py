"""Public Meal Tag Deleted signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_meal_tag_base import PublicMealTagSignalBase


class PublicMealTagDeletedSignal(PublicMealTagSignalBase):
    """Concrete signal: public.meal.tag.deleted"""

    action = SignalActionType.DELETED
