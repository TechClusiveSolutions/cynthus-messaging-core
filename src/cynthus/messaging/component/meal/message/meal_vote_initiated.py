"""Meal Vote Initiated signal message for the Cynthus project"""

from ....common import PublicMealVoteInitiatedSignal, SignalMessage

from ..payload import MealVoteInitiatedPayload


class MealVoteInitiatedMessage(SignalMessage[MealVoteInitiatedPayload]):
    """
        Represents a meal vote initiated signal message

        Emitted by: `cynthus-core-api` when a group meal vote is opened.
        Functional Purpose: Triggers push alerts to group members via `cynthus-messaging` and `cynthus-notification`.
    """

    event_type: str = PublicMealVoteInitiatedSignal.name
