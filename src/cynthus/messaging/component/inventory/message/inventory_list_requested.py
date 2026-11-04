"""Inventory List Requested signal message for the Cynthus project"""

from ....common import PublicInventoryListRequestedSignal, SignalMessage
from ..payload import InventoryListRequestedPayload


class InventoryListRequestedMessage(SignalMessage[InventoryListRequestedPayload]):
    """
        Represents an inventory list requested signal message

        Emitted by: `cynthus-core-api` when a client asks for an inventory listing.
        Functional Purpose: Asks `cynthus-core-inventory` to answer with an inventory list updated message that
        carries the same correlation id.
    """

    event_type: str = PublicInventoryListRequestedSignal.name
