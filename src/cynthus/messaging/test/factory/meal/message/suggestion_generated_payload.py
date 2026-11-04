"""Fixture factory for MealSuggestionGeneratedPayload"""

from uuid import UUID, uuid4

import factory

from .....component.meal.payload import MealSuggestionGeneratedPayload
from ...base_payload_factory import BasePayloadFactory


class MealSuggestionGeneratedPayloadFactory(BasePayloadFactory):
    class Meta:
        model = MealSuggestionGeneratedPayload

    suggestion_id: UUID = factory.LazyFunction(uuid4)
    context_bundle_id: UUID = factory.LazyFunction(uuid4)
