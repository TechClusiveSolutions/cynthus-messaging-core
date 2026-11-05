"""Audit Identity User Rejected signal class for the Cynthus project"""

from .action_type import SignalActionType
from .audit_identity_user_base import AuditIdentityUserSignalBase


class AuditIdentityUserRejectedSignal(AuditIdentityUserSignalBase):
    """Concrete signal: audit.identity.user.rejected"""

    action = SignalActionType.REJECTED
