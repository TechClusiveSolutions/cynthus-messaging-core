"""Public Meal Suggestion Accepted signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_meal_suggestion_base import PublicMealSuggestionSignalBase


class PublicMealSuggestionAcceptedSignal(PublicMealSuggestionSignalBase):
    """Concrete signal: public.meal.suggestion.accepted"""

    action = SignalActionType.ACCEPTED
