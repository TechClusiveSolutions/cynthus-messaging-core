"""Fixture factory for MealSuggestionRejectedMessage"""

import factory

from .....common.signal import LifecycleAction, SignalPayload, PublicMealSuggestionRejectedSignal
from .....component.meal.message import MealSuggestionRejectedMessage

from .suggestion_rejected_payload import MealSuggestionRejectedPayloadFactory

from ...base_message_factory import BaseMessageFactory


class MealSuggestionRejectedMessageFactory(BaseMessageFactory):
    class Meta:
        model = MealSuggestionRejectedMessage

    event_type: str = PublicMealSuggestionRejectedSignal.name
    lifecycle_action: str = LifecycleAction.UPDATED
    payload: SignalPayload = factory.SubFactory(MealSuggestionRejectedPayloadFactory)
        