"""Fixture factory for MealSuggestionGeneratedMessage"""

import factory

from .....common.signal import LifecycleAction, PublicMealSuggestionGeneratedSignal, SignalPayload
from .....component.meal.message import MealSuggestionGeneratedMessage
from ...base_message_factory import BaseMessageFactory
from .suggestion_generated_payload import MealSuggestionGeneratedPayloadFactory


class MealSuggestionGeneratedMessageFactory(BaseMessageFactory):
    class Meta:
        model = MealSuggestionGeneratedMessage

    event_type: str = PublicMealSuggestionGeneratedSignal.name
    lifecycle_action: str = LifecycleAction.CREATED
    payload: SignalPayload = factory.SubFactory(MealSuggestionGeneratedPayloadFactory)
