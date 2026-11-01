"""Meal Suggestion Accepted signal message for the Cynthus project"""

from ....common import PublicMealSuggestionAcceptedSignal, SignalMessage
from ..payload import MealSuggestionAcceptedPayload


class MealSuggestionAcceptedMessage(SignalMessage[MealSuggestionAcceptedPayload]):
    """
        Represents a meal suggestion accepted signal message

        Emitted by: `cynthus-core-api` when a user accepts a meal suggestion.
        Functional Purpose: Stores the acceptance for preference model training in `cynthus-analysis`.
    """

    event_type: str = PublicMealSuggestionAcceptedSignal.name
