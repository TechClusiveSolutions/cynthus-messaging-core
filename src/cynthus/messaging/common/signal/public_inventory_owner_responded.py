"""Public Inventory Owner Responded signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_inventory_owner_base import PublicInventoryOwnerSignalBase


class PublicInventoryOwnerRespondedSignal(PublicInventoryOwnerSignalBase):
    """Concrete signal: public.inventory.owner.responded"""

    action = SignalActionType.RESPONDED
