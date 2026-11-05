"""Issued access token for the Cynthus project"""

from pydantic import BaseModel, ConfigDict, Field


class IssuedToken(BaseModel):
    """A freshly signed access token and the facts about it that are safe to record"""

    model_config = ConfigDict(frozen=True)

    token: str = Field(description='The signed token. Hand it to the caller; never log or record it')
    token_id: str = Field(description='The identifier of the token (its jti claim)')
    key_id: str = Field(description='The identifier of the key that signed the token')
    expires_in: int = Field(description='Seconds until the token expires')
