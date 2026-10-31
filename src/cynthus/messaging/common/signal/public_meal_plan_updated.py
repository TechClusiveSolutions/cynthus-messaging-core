"""Public Meal Plan Updated signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_meal_plan_base import PublicMealPlanSignalBase


class PublicMealPlanUpdatedSignal(PublicMealPlanSignalBase):
    """Concrete signal: public.meal.plan.updated"""

    action = SignalActionType.UPDATED
