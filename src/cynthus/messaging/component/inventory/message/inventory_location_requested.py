"""Inventory Location Requested signal message for the Cynthus project"""

from ....common import PublicInventoryLocationRequestedSignal, SignalMessage
from ..payload import InventoryLocationRequestedPayload


class InventoryLocationRequestedMessage(SignalMessage[InventoryLocationRequestedPayload]):
    """
        Represents an inventory location requested signal message

        Emitted by: `cynthus-core-api` when a caller asks to create, read, change or delete a storage location.
        Functional Purpose: Hands the request to the Inventory service so the caller gets an immediate acknowledgement.
    """

    event_type: str = PublicInventoryLocationRequestedSignal.name
