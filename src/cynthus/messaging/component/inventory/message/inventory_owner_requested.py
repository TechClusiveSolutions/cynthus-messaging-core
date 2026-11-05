"""Inventory Owner Requested signal message for the Cynthus project"""

from ....common import PublicInventoryOwnerRequestedSignal, SignalMessage
from ..payload import InventoryOwnerRequestedPayload


class InventoryOwnerRequestedMessage(SignalMessage[InventoryOwnerRequestedPayload]):
    """
        Represents an inventory owner requested signal message

        Emitted by: `cynthus-core-api` when a caller asks to create, read, change or delete an owner (a user responsible for a shelf).
        Functional Purpose: Hands the request to the Inventory service so the caller gets an immediate acknowledgement.
    """

    event_type: str = PublicInventoryOwnerRequestedSignal.name
