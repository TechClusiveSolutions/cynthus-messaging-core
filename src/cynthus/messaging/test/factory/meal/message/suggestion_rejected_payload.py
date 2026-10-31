"""Fixture factory for MealSuggestionRejectedPayload"""

import factory

from typing import Optional
from uuid import UUID, uuid4

from .....common.signal import DecisionReason
from .....component.meal.payload import MealSuggestionRejectedPayload

from ...base_payload_factory import BasePayloadFactory


class MealSuggestionRejectedPayloadFactory(BasePayloadFactory):
    class Meta:
        model = MealSuggestionRejectedPayload

    suggestion_id: UUID = factory.LazyFunction(uuid4)
    context_bundle_id: UUID = factory.LazyFunction(uuid4)
    reason: Optional[str] = DecisionReason.NOT_SPECIFIED
