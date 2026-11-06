"""Inventory Owner Added signal payload class for the Cynthus project"""

from typing import Optional

from pydantic import Field

from ....common import SignalPayload


class InventoryOwnerAddedPayload(SignalPayload):
    """Represents the payload part of a public.inventory.owner.added signal message"""

    schema_version: int = Field(default=1, ge=1, description='Version of this payload contract')
    shelf_id: str = Field(..., description='The identifier of the shelf')
    owner_id: str = Field(..., description='The identifier of the user')
    granted_by: Optional[str] = Field(default=None, description='The user who granted the ownership')
