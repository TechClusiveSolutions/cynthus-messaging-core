"""Energy Level class for the Cynthus project"""

from enum import Enum


class EnergyLevel(int, Enum):
    VERY_LOW: int = 1
    LOW: int = 3
    MEDIUM: int = 5
    HIGH: int = 7
    VERY_HIGH: int = 9
