"""Identity Access Granted signal payload class for the Cynthus project"""

from typing import Optional

from pydantic import Field

from ....common import SignalPayload


class IdentityAccessGrantedPayload(SignalPayload):
    """Represents the payload part of an audit.identity.access.granted signal message"""

    schema_version: int = Field(default=1, ge=1, description='Version of this payload contract')
    user_id: str = Field(..., description='The identifier of the user')
    token_id: Optional[str] = Field(default=None, description='The identifier of the access token (its jti claim), when it had one')
    permission: str = Field(..., description='The permission the request needed')
    resource: str = Field(..., description='The path of the resource that was requested')
    method: str = Field(..., description='The HTTP method of the request')
