"""Meal Rating Deleted signal message for the Cynthus project"""

from ....common import PublicMealRatingDeletedSignal, SignalMessage
from ..payload import MealRatingDeletedPayload


class MealRatingDeletedMessage(SignalMessage[MealRatingDeletedPayload]):
    """
        Represents a meal rating deleted signal message

        Emitted by: `cynthus-core-api` when a user removes their rating for a meal.
        Functional Purpose: Notifies `cynthus-analysis` to retract the rating from the preference model.
    """

    event_type: str = PublicMealRatingDeletedSignal.name
