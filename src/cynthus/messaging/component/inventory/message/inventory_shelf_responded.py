"""Inventory Shelf Responded signal message for the Cynthus project"""

from ....common import PublicInventoryShelfRespondedSignal, SignalMessage
from ..payload import InventoryShelfRespondedPayload


class InventoryShelfRespondedMessage(SignalMessage[InventoryShelfRespondedPayload]):
    """
        Represents an inventory shelf responded signal message

        Emitted by: `cynthus-inventory` when it has dealt with a request about a shelf within a location.
        Functional Purpose: Carries the outcome back to `cynthus-core-api`, which relays it to the caller.
    """

    event_type: str = PublicInventoryShelfRespondedSignal.name
