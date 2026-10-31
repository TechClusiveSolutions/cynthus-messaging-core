"""Meal Suggestion Requested signal payload class for the Cynthus project"""

from pydantic import Field
from uuid import UUID

from ....common import EnergyLevel, SignalPayload, SignalTriggerType


class MealSuggestionRequestedPayload(SignalPayload):
    """Represents the payload part of a meal.suggestion.requested signal message"""

    context_bundle_id: UUID = Field(..., description='The reference identifier of the assembled context bundle')
    trigger: SignalTriggerType = Field(..., description='The origin of the suggestion request, e.g. on_demand | scheduled')
    energy_level: EnergyLevel = Field(..., description="The user's current Energy Banker spoon budget")
