"""Audit Identity Access Granted signal class for the Cynthus project"""

from .action_type import SignalActionType
from .audit_identity_access_base import AuditIdentityAccessSignalBase


class AuditIdentityAccessGrantedSignal(AuditIdentityAccessSignalBase):
    """Concrete signal: audit.identity.access.granted"""

    action = SignalActionType.GRANTED
