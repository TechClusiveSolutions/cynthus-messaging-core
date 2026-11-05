"""Audit Identity Token Issued signal class for the Cynthus project"""

from .action_type import SignalActionType
from .audit_identity_token_base import AuditIdentityTokenSignalBase


class AuditIdentityTokenIssuedSignal(AuditIdentityTokenSignalBase):
    """Concrete signal: audit.identity.token.issued"""

    action = SignalActionType.ISSUED
