"""Identity Access Denied signal payload class for the Cynthus project"""

from typing import List, Optional

from pydantic import Field

from ....common import SignalPayload


class IdentityAccessDeniedPayload(SignalPayload):
    """Represents the payload part of an audit.identity.access.denied signal message"""

    schema_version: int = Field(default=1, ge=1, description='Version of this payload contract')
    user_id: str = Field(..., description='The identifier of the user')
    token_id: Optional[str] = Field(default=None, description='The identifier of the access token (its jti claim), when it had one')
    required_permission: str = Field(..., description='The permission the request needed')
    granted_permissions: List[str] = Field(default_factory=list, description='The permissions the token carried')
    roles: List[str] = Field(default_factory=list, description='The roles the token carried')
    resource: str = Field(..., description='The path of the resource that was requested')
    method: str = Field(..., description='The HTTP method of the request')
