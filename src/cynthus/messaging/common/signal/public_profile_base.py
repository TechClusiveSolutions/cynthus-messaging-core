"""Public Profile Signal Base class for the Cynthus project"""

from .base import SignalBase
from .domain_type import SignalDomainType


class PublicProfileSignalBase(SignalBase, abstract=True):
    """Intermediate base for all public profile signals. Sets the domain component."""

    domain = SignalDomainType.PROFILE
