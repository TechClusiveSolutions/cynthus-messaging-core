"""Fixture factory for MealSuggestionAcceptedPayload"""

import factory

from typing import Optional
from uuid import UUID, uuid4

from .....common.signal import DecisionReason
from .....component.meal.payload import MealSuggestionAcceptedPayload

from ...base_payload_factory import BasePayloadFactory


class MealSuggestionAcceptedPayloadFactory(BasePayloadFactory):
    class Meta:
        model = MealSuggestionAcceptedPayload

    suggestion_id: UUID = factory.LazyFunction(uuid4)
    context_bundle_id: UUID = factory.LazyFunction(uuid4)
    reason: Optional[str] = DecisionReason.NOT_SPECIFIED
