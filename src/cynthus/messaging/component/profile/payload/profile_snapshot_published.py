"""ProfileSnapshotPublishedPayload signal payload class for the Cynthus project"""

from typing import Any, Dict

from pydantic import Field

from ....common import SignalPayload


class ProfileSnapshotPublishedPayload(SignalPayload):
    """Represents the payload part of a public.profile.snapshot.published signal message"""

    schema_version: int = Field(default=1, ge=1, description='Version of this payload contract')
    user_id: str = Field(..., description='The identifier of the user the profile belongs to')
    profile: Dict[str, Any] = Field(..., description='The whole profile as the Profile service returns it')
    reason: str = Field(default='authentication', description='Why the snapshot was published')
