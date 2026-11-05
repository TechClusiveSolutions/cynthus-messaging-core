"""Public Inventory Item Requested signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_inventory_item_base import PublicInventoryItemSignalBase


class PublicInventoryItemRequestedSignal(PublicInventoryItemSignalBase):
    """Concrete signal: public.inventory.item.requested"""

    action = SignalActionType.REQUESTED
