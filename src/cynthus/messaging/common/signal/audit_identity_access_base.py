"""Audit Identity Access Signal Base class for the Cynthus project"""

from .audit_identity_base import AuditIdentitySignalBase


class AuditIdentityAccessSignalBase(AuditIdentitySignalBase, abstract=True):
    """Intermediate base for all audit identity access signals. Sets the aggregate component."""

    aggregate = 'access'
