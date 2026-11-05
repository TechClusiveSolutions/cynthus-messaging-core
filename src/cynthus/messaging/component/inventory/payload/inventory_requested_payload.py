"""Inventory Requested signal payload base class for the Cynthus project"""

from typing import Any, Dict, Literal, Optional

from pydantic import Field

from ....common import SignalPayload

Operation = Literal['create', 'get', 'list', 'update', 'delete']


class InventoryRequestedPayload(SignalPayload):
    """What a caller asks the Inventory service to do with one kind of inventory record"""

    schema_version: int = Field(default=1, ge=1, description='Version of this payload contract')
    operation: Operation = Field(..., description='What to do: create, get, list, update or delete')
    resource_id: Optional[str] = Field(default=None, description='The record to get, update or delete')
    parent_id: Optional[str] = Field(default=None, description='The shelf an owner belongs to')
    filters: Dict[str, Any] = Field(default_factory=dict, description='Narrows a list, for example type or name')
    data: Dict[str, Any] = Field(default_factory=dict, description='The fields to create or change a record with')
