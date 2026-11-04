"""Public Inventory List Updated signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_inventory_list_base import PublicInventoryListSignalBase


class PublicInventoryListUpdatedSignal(PublicInventoryListSignalBase):
    """Concrete signal: public.inventory.list.updated"""

    action = SignalActionType.UPDATED
