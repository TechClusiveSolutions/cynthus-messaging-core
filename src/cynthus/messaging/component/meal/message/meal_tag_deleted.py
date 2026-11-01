"""Meal Tag Deleted signal message for the Cynthus project"""

from ....common import PublicMealTagDeletedSignal, SignalMessage
from ..payload import MealTagDeletedPayload


class MealTagDeletedMessage(SignalMessage[MealTagDeletedPayload]):
    """
        Represents a meal tag deleted signal message

        Emitted by: `cynthus-core-api` when a tag is removed from a meal entry.
        Functional Purpose: Notifies `cynthus-recipe` and `cynthus-analysis` to remove the tag from preference indexes.
    """

    event_type: str = PublicMealTagDeletedSignal.name
