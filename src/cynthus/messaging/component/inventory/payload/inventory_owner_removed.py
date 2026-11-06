"""Inventory Owner Removed signal payload class for the Cynthus project"""

from pydantic import Field

from ....common import SignalPayload


class InventoryOwnerRemovedPayload(SignalPayload):
    """Represents the payload part of a public.inventory.owner.removed signal message"""

    schema_version: int = Field(default=1, ge=1, description='Version of this payload contract')
    shelf_id: str = Field(..., description='The identifier of the shelf')
    owner_id: str = Field(..., description='The identifier of the user')
