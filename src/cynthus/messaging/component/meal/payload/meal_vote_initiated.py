"""Meal Vote Initiated signal payload class for the Cynthus project"""

from datetime import datetime, timezone

from pydantic import Field, field_serializer

from ....common import SignalPayload


class MealVoteInitiatedPayload(SignalPayload):
    """Represents the payload part of a meal.vote.initiated signal message"""

    vote_id: str = Field(..., description='The identifier of the opened group meal vote')
    group_id: str = Field(..., description='The identifier of the group the vote was opened within')
    proposed_meal: str = Field(..., description='The name of the proposed meal')
    recipe_id: str = Field(..., description='The identifier of the recipe backing the proposed meal')
    expires_at: datetime = Field(..., description='The moment the vote closes')

    @field_serializer('expires_at')
    def serialize_expires_at(self, dt: datetime) -> str:
        """Enforces precise UTC ISO 8601 string formatting on the wire."""

        return dt.astimezone(timezone.utc).isoformat()
