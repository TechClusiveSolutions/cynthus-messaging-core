"""Meal Vote Auto Resolved signal payload class for the Cynthus project"""

from pydantic import Field

from ....common import SignalPayload


class MealVoteAutoResolvedPayload(SignalPayload):
    """Represents the payload part of a meal.vote.auto_resolved signal message"""

    vote_id: str = Field(..., description='The identifier of the stalemated group meal vote')
    group_id: str = Field(..., description='The identifier of the group the vote belongs to')
    resolution: str = Field(..., description='The name of the meal choice Astri selected')
    recipe_id: str = Field(..., description='The identifier of the recipe backing the selected choice')
    tiebreak_rationale: str = Field(..., description="Astri's explanation for the tiebreak decision")
    resolved_by: str = Field(..., description='The identity of the resolving actor, e.g. astri')
