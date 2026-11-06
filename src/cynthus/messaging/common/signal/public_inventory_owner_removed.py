"""Public Inventory Owner Removed signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_inventory_owner_base import PublicInventoryOwnerSignalBase


class PublicInventoryOwnerRemovedSignal(PublicInventoryOwnerSignalBase):
    """Concrete signal: public.inventory.owner.removed"""

    action = SignalActionType.REMOVED
