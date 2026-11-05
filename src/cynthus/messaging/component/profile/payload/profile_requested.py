"""ProfileRequestedPayload signal payload class for the Cynthus project"""

from typing import Any, Dict, Literal, Optional

from pydantic import Field

from ....common import SignalPayload


class ProfileRequestedPayload(SignalPayload):
    """Represents the payload part of a public.profile.profile.requested signal message"""

    schema_version: int = Field(default=1, ge=1, description='Version of this payload contract')
    operation: Literal['create', 'get', 'update', 'delete'] = Field(..., description='What to do: create, get, update or delete')
    resource_id: Optional[str] = Field(default=None, description='The profile to get, update or delete; omitted means the caller\'s own')
    data: Dict[str, Any] = Field(default_factory=dict, description='The fields to create or change the profile with')
