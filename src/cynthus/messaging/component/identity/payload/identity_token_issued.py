"""Identity Token Issued signal payload class for the Cynthus project"""

from typing import List

from pydantic import Field

from ....common import SignalPayload


class IdentityTokenIssuedPayload(SignalPayload):
    """Represents the payload part of an audit.identity.token.issued signal message"""

    schema_version: int = Field(default=1, ge=1, description='Version of this payload contract')
    user_id: str = Field(..., description='The identifier of the user')
    token_id: str = Field(..., description='The identifier of the access token (its jti claim)')
    key_id: str = Field(..., description='The identifier of the key that signed the token')
    expires_in: int = Field(..., description='Seconds until the token expires')
    roles: List[str] = Field(default_factory=list, description='The roles carried by the token')
    permissions: List[str] = Field(default_factory=list, description='The permissions carried by the token')
