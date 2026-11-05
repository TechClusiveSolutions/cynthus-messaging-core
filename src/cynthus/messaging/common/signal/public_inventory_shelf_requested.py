"""Public Inventory Shelf Requested signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_inventory_shelf_base import PublicInventoryShelfSignalBase


class PublicInventoryShelfRequestedSignal(PublicInventoryShelfSignalBase):
    """Concrete signal: public.inventory.shelf.requested"""

    action = SignalActionType.REQUESTED
