"""Identity Access Rejected signal payload class for the Cynthus project"""

from pydantic import Field

from ....common import SignalPayload


class IdentityAccessRejectedPayload(SignalPayload):
    """Represents the payload part of an audit.identity.access.rejected signal message"""

    schema_version: int = Field(default=1, ge=1, description='Version of this payload contract')
    reason: str = Field(..., description='Why the token was not accepted')
    resource: str = Field(..., description='The path of the resource that was requested')
    method: str = Field(..., description='The HTTP method of the request')
