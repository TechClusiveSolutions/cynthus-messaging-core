"""Meal Suggestion Generated signal payload class for the Cynthus project"""

from uuid import UUID

from pydantic import Field

from ....common import SignalPayload


class MealSuggestionGeneratedPayload(SignalPayload):
    """Represents the payload part of a meal.suggestion.generated signal message"""

    suggestion_id: UUID = Field(..., description='The identifier of the generated suggestion')
    context_bundle_id: UUID = Field(..., description='The reference identifier of the context bundle used to generate the suggestion')
