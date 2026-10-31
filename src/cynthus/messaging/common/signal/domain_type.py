"""Signal Domain Type class for the Cynthus project"""

from enum import Enum


class SignalDomainType(str, Enum):
    """Standardized signal domain mutations"""

    MEAL: str = 'meal'
