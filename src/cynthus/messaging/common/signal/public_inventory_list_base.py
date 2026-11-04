"""Public Inventory List Signal Base class for the Cynthus project"""

from .public_inventory_base import PublicInventorySignalBase


class PublicInventoryListSignalBase(PublicInventorySignalBase, abstract=True):
    """Intermediate base for all public inventory list signals. Sets the aggregate component."""

    aggregate = 'list'
