"""Inventory Owner Responded signal message for the Cynthus project"""

from ....common import PublicInventoryOwnerRespondedSignal, SignalMessage
from ..payload import InventoryOwnerRespondedPayload


class InventoryOwnerRespondedMessage(SignalMessage[InventoryOwnerRespondedPayload]):
    """
        Represents an inventory owner responded signal message

        Emitted by: `cynthus-inventory` when it has dealt with a request about an owner (a user responsible for a shelf).
        Functional Purpose: Carries the outcome back to `cynthus-core-api`, which relays it to the caller.
    """

    event_type: str = PublicInventoryOwnerRespondedSignal.name
