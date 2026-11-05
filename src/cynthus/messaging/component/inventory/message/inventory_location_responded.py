"""Inventory Location Responded signal message for the Cynthus project"""

from ....common import PublicInventoryLocationRespondedSignal, SignalMessage
from ..payload import InventoryLocationRespondedPayload


class InventoryLocationRespondedMessage(SignalMessage[InventoryLocationRespondedPayload]):
    """
        Represents an inventory location responded signal message

        Emitted by: `cynthus-inventory` when it has dealt with a request about a storage location.
        Functional Purpose: Carries the outcome back to `cynthus-core-api`, which relays it to the caller.
    """

    event_type: str = PublicInventoryLocationRespondedSignal.name
