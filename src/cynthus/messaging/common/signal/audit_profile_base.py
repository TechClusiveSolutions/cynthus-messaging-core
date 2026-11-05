"""Audit Profile Signal Base class for the Cynthus project"""

from .base import SignalBase
from .domain_type import SignalDomainType


class AuditProfileSignalBase(SignalBase, abstract=True):
    """Intermediate base for all audit profile signals. Sets the visibility and domain components."""

    visibility = 'audit'
    domain = SignalDomainType.PROFILE
