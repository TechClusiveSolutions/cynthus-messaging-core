"""Meal Suggestion Generated signal message for the Cynthus project"""

from ....common import PublicMealSuggestionGeneratedSignal, SignalMessage
from ..payload import MealSuggestionGeneratedPayload


class MealSuggestionGeneratedMessage(SignalMessage[MealSuggestionGeneratedPayload]):
    """
        Represents a meal suggestion generated signal message

        Emitted by: `cynthus-chat` when Astri produces a meal suggestion and returns it to the user.
        Functional Purpose: Notifies `cynthus-core-api` and `cynthus-analysis` of the generated suggestion.
    """

    event_type: str = PublicMealSuggestionGeneratedSignal.name
