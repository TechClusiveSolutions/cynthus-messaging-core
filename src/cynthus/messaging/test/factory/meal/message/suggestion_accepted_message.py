"""Fixture factory for MealSuggestionAcceptedMessage"""

import factory

from .....common.signal import LifecycleAction, PublicMealSuggestionAcceptedSignal, SignalPayload
from .....component.meal.message import MealSuggestionAcceptedMessage
from ...base_message_factory import BaseMessageFactory
from .suggestion_accepted_payload import MealSuggestionAcceptedPayloadFactory


class MealSuggestionAcceptedMessageFactory(BaseMessageFactory):
    class Meta:
        model = MealSuggestionAcceptedMessage

    event_type: str = PublicMealSuggestionAcceptedSignal.name
    lifecycle_action: str = LifecycleAction.UPDATED
    payload: SignalPayload = factory.SubFactory(MealSuggestionAcceptedPayloadFactory)
