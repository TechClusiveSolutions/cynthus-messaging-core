"""Meal Tag Created signal message for the Cynthus project"""

from ....common import PublicMealTagCreatedSignal, SignalMessage
from ..payload import MealTagCreatedPayload


class MealTagCreatedMessage(SignalMessage[MealTagCreatedPayload]):
    """
        Represents a meal tag created signal message

        Emitted by: `cynthus-core-api` when a tag is applied to a meal entry.
        Functional Purpose: Notifies `cynthus-recipe` and `cynthus-analysis` of the new tag for preference indexing.
    """

    event_type: str = PublicMealTagCreatedSignal.name
