"""Identity User Authenticated signal payload class for the Cynthus project"""

from pydantic import Field

from ....common import SignalPayload


class IdentityUserAuthenticatedPayload(SignalPayload):
    """Represents the payload part of an audit.identity.user.authenticated signal message"""

    schema_version: int = Field(default=1, ge=1, description='Version of this payload contract')
    user_id: str = Field(..., description='The identifier of the user')
    username: str = Field(..., description='The username that was presented')
    method: str = Field(default='password', description='How the user proved who they are')
