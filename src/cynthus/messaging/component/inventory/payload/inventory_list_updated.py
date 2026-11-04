"""Inventory List Updated signal payload class for the Cynthus project"""

from typing import Any, Dict, List

from pydantic import Field

from ....common import SignalPayload


class InventoryListUpdatedPayload(SignalPayload):
    """Represents the payload part of a public.inventory.list.updated signal message"""

    schema_version: int = Field(default=1, ge=1, description='Version of this payload contract')
    items: List[Dict[str, Any]] = Field(default_factory=list, description='The inventory items that match the query')
