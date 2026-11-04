"""Fixture factory for MealSuggestionRequestedMessage"""

import factory

from .....common.signal import LifecycleAction, PublicMealSuggestionRequestedSignal, SignalPayload
from .....component.meal.message import MealSuggestionRequestedMessage
from ...base_message_factory import BaseMessageFactory
from .suggestion_requested_payload import MealSuggestionRequestedPayloadFactory


class MealSuggestionRequestedMessageFactory(BaseMessageFactory):
    class Meta:
        model = MealSuggestionRequestedMessage

    event_type: str = PublicMealSuggestionRequestedSignal.name
    lifecycle_action: str = LifecycleAction.CREATED
    payload: SignalPayload = factory.SubFactory(MealSuggestionRequestedPayloadFactory)
