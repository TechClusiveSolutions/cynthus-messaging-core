"""Public Meal Suggestion Generated signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_meal_suggestion_base import PublicMealSuggestionSignalBase


class PublicMealSuggestionGeneratedSignal(PublicMealSuggestionSignalBase):
    """Concrete signal: public.meal.suggestion.generated"""

    action = SignalActionType.GENERATED
