"""Signal Domain Type class for the Cynthus project"""

from enum import Enum


class SignalDomainType(str, Enum):
    """Standardized signal domain mutations"""

    INVENTORY: str = 'inventory'
    MEAL: str = 'meal'
