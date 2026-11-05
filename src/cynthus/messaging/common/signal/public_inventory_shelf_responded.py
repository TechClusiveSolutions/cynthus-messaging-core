"""Public Inventory Shelf Responded signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_inventory_shelf_base import PublicInventoryShelfSignalBase


class PublicInventoryShelfRespondedSignal(PublicInventoryShelfSignalBase):
    """Concrete signal: public.inventory.shelf.responded"""

    action = SignalActionType.RESPONDED
