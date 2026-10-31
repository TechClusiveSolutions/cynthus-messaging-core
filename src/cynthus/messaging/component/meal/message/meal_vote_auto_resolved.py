"""Meal Vote Auto Resolved signal message for the Cynthus project"""

from ....common import PublicMealVoteAutoResolvedSignal, SignalMessage

from ..payload import MealVoteAutoResolvedPayload


class MealVoteAutoResolvedMessage(SignalMessage[MealVoteAutoResolvedPayload]):
    """
        Represents a meal vote auto resolved signal message

        Emitted by: `cynthus-chat` when Astri resolves a stalemated group meal vote.
        Functional Purpose: Notifies `cynthus-core-api` and `cynthus-notification` of the tiebreak resolution.
    """

    event_type: str = PublicMealVoteAutoResolvedSignal.name
