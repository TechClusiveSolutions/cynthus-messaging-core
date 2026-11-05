"""Public Inventory Owner Requested signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_inventory_owner_base import PublicInventoryOwnerSignalBase


class PublicInventoryOwnerRequestedSignal(PublicInventoryOwnerSignalBase):
    """Concrete signal: public.inventory.owner.requested"""

    action = SignalActionType.REQUESTED
