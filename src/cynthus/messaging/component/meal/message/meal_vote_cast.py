"""Meal Vote Cast signal message for the Cynthus project"""

from ....common import PublicMealVoteCastSignal, SignalMessage
from ..payload import MealVoteCastPayload


class MealVoteCastMessage(SignalMessage[MealVoteCastPayload]):
    """
        Represents a meal vote cast signal message

        Emitted by: `cynthus-core-api` when a group member submits their vote.
        Functional Purpose: Updates the running tally for `cynthus-analysis` and `cynthus-messaging`.
    """

    event_type: str = PublicMealVoteCastSignal.name
