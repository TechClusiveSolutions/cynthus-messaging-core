"""Fixture factory for MealSuggestionRequestedPayload"""

import factory

from uuid import UUID, uuid4

from .....common.signal import EnergyLevel, SignalTriggerType
from .....component.meal.payload import MealSuggestionRequestedPayload

from ...base_payload_factory import BasePayloadFactory


class MealSuggestionRequestedPayloadFactory(BasePayloadFactory):
    class Meta:
        model = MealSuggestionRequestedPayload

    # There is no suggestion_id here. It hasn't been created yet
    context_bundle_id: UUID = factory.LazyFunction(uuid4)
    trigger: str = SignalTriggerType.ACTION_PERFORMED
    energy_level: int = EnergyLevel.MEDIUM
