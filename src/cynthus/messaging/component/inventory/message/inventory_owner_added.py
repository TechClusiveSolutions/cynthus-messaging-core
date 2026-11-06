"""Inventory Owner Added signal message for the Cynthus project"""

from ....common import PublicInventoryOwnerAddedSignal, SignalMessage
from ..payload import InventoryOwnerAddedPayload


class InventoryOwnerAddedMessage(SignalMessage[InventoryOwnerAddedPayload]):
    """
        Represents an inventory owner added signal message

        Emitted by: `cynthus-inventory` when a user is added to the owners of a shelf.
        Functional Purpose: Lets subscribers follow ownership changes without asking the Inventory service.
    """

    event_type: str = PublicInventoryOwnerAddedSignal.name
