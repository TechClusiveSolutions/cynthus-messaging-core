"""Fixture factory for MealSuggestionRequestedMessage"""

import factory

from .....common.signal import LifecycleAction, SignalPayload, PublicMealSuggestionRequestedSignal
from .....component.meal.message import MealSuggestionRequestedMessage

from .suggestion_requested_payload import MealSuggestionRequestedPayloadFactory

from ...base_message_factory import BaseMessageFactory


class MealSuggestionRequestedMessageFactory(BaseMessageFactory):
    class Meta:
        model = MealSuggestionRequestedMessage

    event_type: str = PublicMealSuggestionRequestedSignal.name
    lifecycle_action: str = LifecycleAction.CREATED
    payload: SignalPayload = factory.SubFactory(MealSuggestionRequestedPayloadFactory)
        