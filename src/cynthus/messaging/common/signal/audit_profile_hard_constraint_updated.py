"""Audit Profile HardConstraint Updated signal class for the Cynthus project"""

from .action_type import SignalActionType
from .audit_profile_hard_constraint_base import AuditProfileHardConstraintSignalBase


class AuditProfileHardConstraintUpdatedSignal(AuditProfileHardConstraintSignalBase):
    """Concrete signal: audit.profile.hard_constraint.updated"""

    action = SignalActionType.UPDATED
