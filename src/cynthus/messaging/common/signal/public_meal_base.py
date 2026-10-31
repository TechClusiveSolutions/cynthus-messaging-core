"""Public Meal Signal Base class for the Cynthus project"""

from .base import SignalBase
from .domain_type import SignalDomainType


class PublicMealSignalBase(SignalBase, abstract=True):
    """Intermediate base for all public meal signals. Sets the domain component."""

    domain = SignalDomainType.MEAL
