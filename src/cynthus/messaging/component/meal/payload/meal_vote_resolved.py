"""Meal Vote Resolved signal payload class for the Cynthus project"""

from pydantic import Field

from ....common import SignalPayload


class MealVoteResolvedPayload(SignalPayload):
    """Represents the payload part of a meal.vote.resolved signal message"""

    vote_id: str = Field(..., description='The identifier of the concluded group meal vote')
    group_id: str = Field(..., description='The identifier of the group the vote belongs to')
    resolution: str = Field(..., description='The name of the winning meal choice')
    recipe_id: str = Field(..., description='The identifier of the recipe backing the winning choice')
