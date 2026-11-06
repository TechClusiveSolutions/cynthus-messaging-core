"""Public Inventory Owner Added signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_inventory_owner_base import PublicInventoryOwnerSignalBase


class PublicInventoryOwnerAddedSignal(PublicInventoryOwnerSignalBase):
    """Concrete signal: public.inventory.owner.added"""

    action = SignalActionType.ADDED
