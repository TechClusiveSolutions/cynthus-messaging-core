"""Public Inventory Item Responded signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_inventory_item_base import PublicInventoryItemSignalBase


class PublicInventoryItemRespondedSignal(PublicInventoryItemSignalBase):
    """Concrete signal: public.inventory.item.responded"""

    action = SignalActionType.RESPONDED
