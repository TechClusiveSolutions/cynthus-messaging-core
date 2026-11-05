"""Audit Identity User Signal Base class for the Cynthus project"""

from .audit_identity_base import AuditIdentitySignalBase


class AuditIdentityUserSignalBase(AuditIdentitySignalBase, abstract=True):
    """Intermediate base for all audit identity user signals. Sets the aggregate component."""

    aggregate = 'user'
