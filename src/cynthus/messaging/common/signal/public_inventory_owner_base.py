"""Public Inventory Owner Signal Base class for the Cynthus project"""

from .public_inventory_base import PublicInventorySignalBase


class PublicInventoryOwnerSignalBase(PublicInventorySignalBase, abstract=True):
    """Intermediate base for all public inventory owner signals. Sets the aggregate component."""

    aggregate = 'owner'
