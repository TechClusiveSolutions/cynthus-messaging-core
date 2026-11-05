"""Audit Profile HardConstraint Signal Base class for the Cynthus project"""

from .audit_profile_base import AuditProfileSignalBase


class AuditProfileHardConstraintSignalBase(AuditProfileSignalBase, abstract=True):
    """Intermediate base for all audit profile hard constraint signals. Sets the aggregate component."""

    aggregate = 'hard_constraint'
