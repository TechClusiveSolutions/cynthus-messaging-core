"""Inventory List Updated signal message for the Cynthus project"""

from ....common import PublicInventoryListUpdatedSignal, SignalMessage
from ..payload import InventoryListUpdatedPayload


class InventoryListUpdatedMessage(SignalMessage[InventoryListUpdatedPayload]):
    """
        Represents an inventory list updated signal message

        Emitted by: `cynthus-core-inventory` in answer to an inventory list requested message.
        Functional Purpose: Lets `cynthus-core-api` push the listing to the client that asked for it.
    """

    event_type: str = PublicInventoryListUpdatedSignal.name
