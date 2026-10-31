"""Public Meal Suggestion Requested signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_meal_suggestion_base import PublicMealSuggestionSignalBase


class PublicMealSuggestionRequestedSignal(PublicMealSuggestionSignalBase):
    """Concrete signal: public.meal.suggestion.requested"""

    action = SignalActionType.REQUESTED
