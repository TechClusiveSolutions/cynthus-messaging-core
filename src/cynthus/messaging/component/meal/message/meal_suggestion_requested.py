"""Meal Suggestion Requested signal message for the Cynthus project"""

from ....common import PublicMealSuggestionRequestedSignal, SignalMessage
from ..payload import MealSuggestionRequestedPayload


class MealSuggestionRequestedMessage(SignalMessage[MealSuggestionRequestedPayload]):
    """
        Represents a meal suggestion requested signal message

        Emitted by: `cynthus-core-api` when a user initiates an on-demand meal suggestion.
        Functional Purpose: Forwards the context bundle reference to `cynthus-chat` so Astri can produce a suggestion.
    """

    event_type: str = PublicMealSuggestionRequestedSignal.name
