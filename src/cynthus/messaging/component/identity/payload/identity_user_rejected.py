"""Identity User Rejected signal payload class for the Cynthus project"""

from pydantic import Field

from ....common import SignalPayload


class IdentityUserRejectedPayload(SignalPayload):
    """Represents the payload part of an audit.identity.user.rejected signal message"""

    schema_version: int = Field(default=1, ge=1, description='Version of this payload contract')
    username: str = Field(..., description='The username that was presented')
    reason: str = Field(default='invalid_credentials', description='Why the sign-in was refused')
