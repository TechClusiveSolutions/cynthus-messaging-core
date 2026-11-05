"""ProfileDeletedPayload signal payload class for the Cynthus project"""

from typing import List

from pydantic import Field

from ....common import SignalPayload


class ProfileDeletedPayload(SignalPayload):
    """Represents the payload part of a public.profile.profile.deleted signal message"""

    schema_version: int = Field(default=1, ge=1, description='Version of this payload contract')
    profile_id: str = Field(..., description='The identifier of the profile')
    user_id: str = Field(..., description='The identifier of the user the profile belongs to')
    changed: List[str] = Field(default_factory=list, description='Which parts changed: display_name, allergies, likes, dislikes, favorites or conditions')
