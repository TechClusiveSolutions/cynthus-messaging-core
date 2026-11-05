"""Audit Identity Access Denied signal class for the Cynthus project"""

from .action_type import SignalActionType
from .audit_identity_access_base import AuditIdentityAccessSignalBase


class AuditIdentityAccessDeniedSignal(AuditIdentityAccessSignalBase):
    """Concrete signal: audit.identity.access.denied"""

    action = SignalActionType.DENIED
