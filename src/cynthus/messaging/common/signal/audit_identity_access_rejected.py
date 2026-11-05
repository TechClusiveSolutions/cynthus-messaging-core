"""Audit Identity Access Rejected signal class for the Cynthus project"""

from .action_type import SignalActionType
from .audit_identity_access_base import AuditIdentityAccessSignalBase


class AuditIdentityAccessRejectedSignal(AuditIdentityAccessSignalBase):
    """Concrete signal: audit.identity.access.rejected"""

    action = SignalActionType.REJECTED
