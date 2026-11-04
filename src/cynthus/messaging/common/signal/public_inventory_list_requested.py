"""Public Inventory List Requested signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_inventory_list_base import PublicInventoryListSignalBase


class PublicInventoryListRequestedSignal(PublicInventoryListSignalBase):
    """Concrete signal: public.inventory.list.requested"""

    action = SignalActionType.REQUESTED
