"""Meal Vote Cast signal payload class for the Cynthus project"""

from typing import Dict

from pydantic import Field

from ....common import SignalPayload


class MealVoteCastPayload(SignalPayload):
    """Represents the payload part of a meal.vote.cast signal message"""

    vote_id: str = Field(..., description='The identifier of the group meal vote')
    group_id: str = Field(..., description='The identifier of the group the vote belongs to')
    vote: str = Field(..., description="The voter's submitted choice, e.g. yes | no | pending")
    current_tally: Dict[str, int] = Field(..., description='The running tally of votes by choice')
