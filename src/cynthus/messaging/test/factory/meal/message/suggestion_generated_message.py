"""Fixture factory for MealSuggestionGeneratedMessage"""

import factory

from .....common.signal import LifecycleAction, SignalPayload, PublicMealSuggestionGeneratedSignal
from .....component.meal.message import MealSuggestionGeneratedMessage

from .suggestion_generated_payload import MealSuggestionGeneratedPayloadFactory

from ...base_message_factory import BaseMessageFactory


class MealSuggestionGeneratedMessageFactory(BaseMessageFactory):
    class Meta:
        model = MealSuggestionGeneratedMessage

    event_type: str = PublicMealSuggestionGeneratedSignal.name
    lifecycle_action: str = LifecycleAction.CREATED
    payload: SignalPayload = factory.SubFactory(MealSuggestionGeneratedPayloadFactory)
        