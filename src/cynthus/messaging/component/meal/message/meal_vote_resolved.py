"""Meal Vote Resolved signal message for the Cynthus project"""

from ....common import PublicMealVoteResolvedSignal, SignalMessage

from ..payload import MealVoteResolvedPayload


class MealVoteResolvedMessage(SignalMessage[MealVoteResolvedPayload]):
    """
        Represents a meal vote resolved signal message

        Emitted by: `cynthus-core-api` when a group meal vote concludes with a winning choice.
        Functional Purpose: Notifies `cynthus-chat` and `cynthus-notification` of the resolution.
    """

    event_type: str = PublicMealVoteResolvedSignal.name
