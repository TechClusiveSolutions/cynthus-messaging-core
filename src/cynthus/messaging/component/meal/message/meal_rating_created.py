"""Meal Rating Created signal message for the Cynthus project"""

from ....common import PublicMealRatingCreatedSignal, SignalMessage

from ..payload import MealRatingCreatedPayload


class MealRatingCreatedMessage(SignalMessage[MealRatingCreatedPayload]):
    """
        Represents a meal rating created signal message

        Emitted by: `cynthus-core-api` when a user submits a rating for a meal.
        Functional Purpose: Notifies `cynthus-analysis` to incorporate the rating into the preference model.
    """

    event_type: str = PublicMealRatingCreatedSignal.name
