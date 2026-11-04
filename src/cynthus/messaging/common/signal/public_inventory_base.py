"""Public Inventory Signal Base class for the Cynthus project"""

from .base import SignalBase
from .domain_type import SignalDomainType


class PublicInventorySignalBase(SignalBase, abstract=True):
    """Intermediate base for all public inventory signals. Sets the domain component."""

    domain = SignalDomainType.INVENTORY
