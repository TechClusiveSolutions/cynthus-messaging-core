"""Inventory Responded signal payload base class for the Cynthus project"""

from typing import Any, Optional

from pydantic import Field

from ....common import SignalPayload


class InventoryRespondedPayload(SignalPayload):
    """How the Inventory service answered a request, with an HTTP-style status"""

    schema_version: int = Field(default=1, ge=1, description='Version of this payload contract')
    operation: str = Field(..., description='The operation that was requested')
    status: int = Field(..., description='200, 201 or 204 when it worked; 401, 403, 404, 409 or 422 when it did not')
    result: Optional[Any] = Field(default=None, description='The record, or the list of records, when it worked')
    error: Optional[str] = Field(default=None, description='Why the request failed')
