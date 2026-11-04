"""Meal Suggestion Accepted signal payload class for the Cynthus project"""

from typing import Optional
from uuid import UUID

from pydantic import Field

from ....common import DecisionReason, SignalPayload


class MealSuggestionAcceptedPayload(SignalPayload):
    """Represents the payload part of a meal.suggestion.accepted signal message"""

    suggestion_id: UUID = Field(..., description='The identifier of the accepted suggestion')
    context_bundle_id: UUID = Field(..., description='The reference identifier of the context bundle that produced this suggestion')
    reason: Optional[str] = Field(DecisionReason.NOT_SPECIFIED, description='The reason the user rejected the suggestion; absent when the user declines without explanation')
