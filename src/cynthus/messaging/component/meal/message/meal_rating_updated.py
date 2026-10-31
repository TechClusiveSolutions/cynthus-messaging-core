"""Meal Rating Updated signal message for the Cynthus project"""

from ....common import PublicMealRatingUpdatedSignal, SignalMessage

from ..payload import MealRatingUpdatedPayload


class MealRatingUpdatedMessage(SignalMessage[MealRatingUpdatedPayload]):
    """
        Represents a meal rating updated signal message

        Emitted by: `cynthus-core-api` when a user revises their rating for a meal.
        Functional Purpose: Notifies `cynthus-analysis` to update the rating in the preference model.
    """

    event_type: str = PublicMealRatingUpdatedSignal.name
