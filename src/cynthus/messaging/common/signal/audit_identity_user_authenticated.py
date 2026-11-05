"""Audit Identity User Authenticated signal class for the Cynthus project"""

from .action_type import SignalActionType
from .audit_identity_user_base import AuditIdentityUserSignalBase


class AuditIdentityUserAuthenticatedSignal(AuditIdentityUserSignalBase):
    """Concrete signal: audit.identity.user.authenticated"""

    action = SignalActionType.AUTHENTICATED
