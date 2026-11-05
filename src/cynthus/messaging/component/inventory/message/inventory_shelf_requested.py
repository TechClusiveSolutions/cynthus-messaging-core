"""Inventory Shelf Requested signal message for the Cynthus project"""

from ....common import PublicInventoryShelfRequestedSignal, SignalMessage
from ..payload import InventoryShelfRequestedPayload


class InventoryShelfRequestedMessage(SignalMessage[InventoryShelfRequestedPayload]):
    """
        Represents an inventory shelf requested signal message

        Emitted by: `cynthus-core-api` when a caller asks to create, read, change or delete a shelf within a location.
        Functional Purpose: Hands the request to the Inventory service so the caller gets an immediate acknowledgement.
    """

    event_type: str = PublicInventoryShelfRequestedSignal.name
