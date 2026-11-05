"""Identity Access Rejected signal message for the Cynthus project"""

from ....common import AuditIdentityAccessRejectedSignal, SignalMessage
from ..payload import IdentityAccessRejectedPayload


class IdentityAccessRejectedMessage(SignalMessage[IdentityAccessRejectedPayload]):
    """
        Represents an identity access rejected signal message

        Emitted by: the service that checked the request when a request has no valid token (missing, malformed, expired, forged or for another caller).
        Functional Purpose: Authentication failure (HTTP 401). Lets `cynthus-audit` and security monitoring see attempts without a valid identity.
    """

    event_type: str = AuditIdentityAccessRejectedSignal.name
