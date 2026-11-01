"""Public Meal Suggestion Rejected signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_meal_suggestion_base import PublicMealSuggestionSignalBase


class PublicMealSuggestionRejectedSignal(PublicMealSuggestionSignalBase):
    """Concrete signal: public.meal.suggestion.rejected"""

    action = SignalActionType.REJECTED
