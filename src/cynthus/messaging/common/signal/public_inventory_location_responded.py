"""Public Inventory Location Responded signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_inventory_location_base import PublicInventoryLocationSignalBase


class PublicInventoryLocationRespondedSignal(PublicInventoryLocationSignalBase):
    """Concrete signal: public.inventory.location.responded"""

    action = SignalActionType.RESPONDED
