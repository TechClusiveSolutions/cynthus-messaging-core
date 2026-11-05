"""Audit Identity Token Signal Base class for the Cynthus project"""

from .audit_identity_base import AuditIdentitySignalBase


class AuditIdentityTokenSignalBase(AuditIdentitySignalBase, abstract=True):
    """Intermediate base for all audit identity token signals. Sets the aggregate component."""

    aggregate = 'token'
