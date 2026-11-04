"""Inventory List Requested signal payload class for the Cynthus project"""

from typing import Optional

from pydantic import Field

from ....common import SignalPayload


class InventoryListRequestedPayload(SignalPayload):
    """Represents the payload part of a public.inventory.list.requested signal message"""

    schema_version: int = Field(default=1, ge=1, description='Version of this payload contract')
    item_type: Optional[str] = Field(default=None, description='Only list items of this type, for example frozen')
    name: Optional[str] = Field(default=None, description='Only list items whose name matches this text')
