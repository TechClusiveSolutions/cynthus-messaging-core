"""Public Meal Plan Deleted signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_meal_plan_base import PublicMealPlanSignalBase


class PublicMealPlanDeletedSignal(PublicMealPlanSignalBase):
    """Concrete signal: public.meal.plan.deleted"""

    action = SignalActionType.DELETED
