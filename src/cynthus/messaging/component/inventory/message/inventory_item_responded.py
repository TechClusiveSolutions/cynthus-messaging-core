"""Inventory Item Responded signal message for the Cynthus project"""

from ....common import PublicInventoryItemRespondedSignal, SignalMessage
from ..payload import InventoryItemRespondedPayload


class InventoryItemRespondedMessage(SignalMessage[InventoryItemRespondedPayload]):
    """
        Represents an inventory item responded signal message

        Emitted by: `cynthus-inventory` when it has dealt with a request about an item on a shelf.
        Functional Purpose: Carries the outcome back to `cynthus-core-api`, which relays it to the caller.
    """

    event_type: str = PublicInventoryItemRespondedSignal.name
