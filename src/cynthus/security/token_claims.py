"""Access token claims for the Cynthus project"""

from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class TokenClaims(BaseModel):
    """What a verified access token says about its holder"""

    model_config = ConfigDict(frozen=True)

    subject: UUID = Field(description='The user the token was issued to (the `sub` claim)')
    organization_id: UUID = Field(description='The corporate tenant the user belongs to')
    workspace_id: UUID = Field(description='The workspace the token is valid for')
    token_id: Optional[str] = Field(default=None, description='The identifier of the token (the `jti` claim)')
    roles: List[str] = Field(default_factory=list, description='Roles granted to the user')
    permissions: List[str] = Field(default_factory=list, description='Permissions such as inventory:read')
    issued_at: int = Field(description='Seconds since the epoch when the token was issued')
    expires_at: int = Field(description='Seconds since the epoch when the token stops being valid')

    def has_permission(self, permission: str) -> bool:
        return permission in self.permissions
