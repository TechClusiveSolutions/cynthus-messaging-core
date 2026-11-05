"""Identity Token Issued signal message for the Cynthus project"""

from ....common import AuditIdentityTokenIssuedSignal, SignalMessage
from ..payload import IdentityTokenIssuedPayload


class IdentityTokenIssuedMessage(SignalMessage[IdentityTokenIssuedPayload]):
    """
        Represents an identity token issued signal message

        Emitted by: `cynthus-auth` when an access token is issued.
        Functional Purpose: Records which token was issued to whom and with which permissions. The token itself is never included.
    """

    event_type: str = AuditIdentityTokenIssuedSignal.name
