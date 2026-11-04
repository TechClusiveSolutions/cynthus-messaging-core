"""Meal Suggestion Denied signal message for the Cynthus project"""

from ....common import PublicMealSuggestionRejectedSignal, SignalMessage
from ..payload import MealSuggestionRejectedPayload


class MealSuggestionRejectedMessage(SignalMessage[MealSuggestionRejectedPayload]):
    """
        Represents a meal suggestion rejected signal message

        Emitted by: `cynthus-core-api` when a user denies a meal suggestion.
        Functional Purpose: Triggers a follow-up suggestion from Astri via `cynthus-chat`.
    """

    event_type: str = PublicMealSuggestionRejectedSignal.name
