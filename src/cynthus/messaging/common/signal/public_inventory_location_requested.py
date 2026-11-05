"""Public Inventory Location Requested signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_inventory_location_base import PublicInventoryLocationSignalBase


class PublicInventoryLocationRequestedSignal(PublicInventoryLocationSignalBase):
    """Concrete signal: public.inventory.location.requested"""

    action = SignalActionType.REQUESTED
