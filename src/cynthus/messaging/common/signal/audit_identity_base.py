"""Audit Identity Signal Base class for the Cynthus project"""

from .base import SignalBase
from .domain_type import SignalDomainType


class AuditIdentitySignalBase(SignalBase, abstract=True):
    """Intermediate base for all audit identity signals. Sets the visibility and domain components."""

    visibility = 'audit'
    domain = SignalDomainType.IDENTITY
