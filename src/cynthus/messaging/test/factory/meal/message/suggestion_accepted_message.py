"""Fixture factory for MealSuggestionAcceptedMessage"""

import factory

from .....common.signal import LifecycleAction, SignalPayload, PublicMealSuggestionAcceptedSignal
from .....component.meal.message import MealSuggestionAcceptedMessage

from .suggestion_accepted_payload import MealSuggestionAcceptedPayloadFactory

from ...base_message_factory import BaseMessageFactory


class MealSuggestionAcceptedMessageFactory(BaseMessageFactory):
    class Meta:
        model = MealSuggestionAcceptedMessage

    event_type: str = PublicMealSuggestionAcceptedSignal.name
    lifecycle_action: str = LifecycleAction.UPDATED
    payload: SignalPayload = factory.SubFactory(MealSuggestionAcceptedPayloadFactory)
        