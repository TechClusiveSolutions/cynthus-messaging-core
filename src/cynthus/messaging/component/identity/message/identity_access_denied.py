"""Identity Access Denied signal message for the Cynthus project"""

from ....common import AuditIdentityAccessDeniedSignal, SignalMessage
from ..payload import IdentityAccessDeniedPayload


class IdentityAccessDeniedMessage(SignalMessage[IdentityAccessDeniedPayload]):
    """
        Represents an identity access denied signal message

        Emitted by: the service that checked the request when a request has a valid token that does not grant the permission it needs.
        Functional Purpose: Authorization failure (HTTP 403), the role-based access violation. Lets `cynthus-audit` and security monitoring see users reaching beyond their role.
    """

    event_type: str = AuditIdentityAccessDeniedSignal.name
