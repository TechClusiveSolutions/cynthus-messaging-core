"""Identity Access Granted signal message for the Cynthus project"""

from ....common import AuditIdentityAccessGrantedSignal, SignalMessage
from ..payload import IdentityAccessGrantedPayload


class IdentityAccessGrantedMessage(SignalMessage[IdentityAccessGrantedPayload]):
    """
        Represents an identity access granted signal message

        Emitted by: the service that checked the request when a request is let through.
        Functional Purpose: Records who used which permission on which resource.
    """

    event_type: str = AuditIdentityAccessGrantedSignal.name
