"""Public Meal Plan Created signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_meal_plan_base import PublicMealPlanSignalBase


class PublicMealPlanCreatedSignal(PublicMealPlanSignalBase):
    """Concrete signal: public.meal.plan.created"""

    action = SignalActionType.CREATED
