"""Fixture factory for MealSuggestionRejectedMessage"""

import factory

from .....common.signal import LifecycleAction, PublicMealSuggestionRejectedSignal, SignalPayload
from .....component.meal.message import MealSuggestionRejectedMessage
from ...base_message_factory import BaseMessageFactory
from .suggestion_rejected_payload import MealSuggestionRejectedPayloadFactory


class MealSuggestionRejectedMessageFactory(BaseMessageFactory):
    class Meta:
        model = MealSuggestionRejectedMessage

    event_type: str = PublicMealSuggestionRejectedSignal.name
    lifecycle_action: str = LifecycleAction.UPDATED
    payload: SignalPayload = factory.SubFactory(MealSuggestionRejectedPayloadFactory)
