"""Inventory Owner Removed signal message for the Cynthus project"""

from ....common import PublicInventoryOwnerRemovedSignal, SignalMessage
from ..payload import InventoryOwnerRemovedPayload


class InventoryOwnerRemovedMessage(SignalMessage[InventoryOwnerRemovedPayload]):
    """
        Represents an inventory owner removed signal message

        Emitted by: `cynthus-inventory` when a user is removed from the owners of a shelf.
        Functional Purpose: Lets subscribers follow ownership changes without asking the Inventory service.
    """

    event_type: str = PublicInventoryOwnerRemovedSignal.name
