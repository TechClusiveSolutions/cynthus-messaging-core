"""Inventory Item Requested signal message for the Cynthus project"""

from ....common import PublicInventoryItemRequestedSignal, SignalMessage
from ..payload import InventoryItemRequestedPayload


class InventoryItemRequestedMessage(SignalMessage[InventoryItemRequestedPayload]):
    """
        Represents an inventory item requested signal message

        Emitted by: `cynthus-core-api` when a caller asks to create, read, change or delete an item on a shelf.
        Functional Purpose: Hands the request to the Inventory service so the caller gets an immediate acknowledgement.
    """

    event_type: str = PublicInventoryItemRequestedSignal.name
