"""ProfileHardConstraintUpdatedPayload signal payload class for the Cynthus project"""

from typing import List

from pydantic import Field

from ....common import SignalPayload


class ProfileHardConstraintUpdatedPayload(SignalPayload):
    """Represents the payload part of a audit.profile.hard_constraint.updated signal message"""

    schema_version: int = Field(default=1, ge=1, description='Version of this payload contract')
    user_id: str = Field(..., description='The identifier of the user the profile belongs to')
    profile_id: str = Field(..., description='The identifier of the profile')
    kind: str = Field(..., description='allergy or condition')
    added: List[str] = Field(default_factory=list, description='The entries being added')
    removed: List[str] = Field(default_factory=list, description='The entries being removed')
