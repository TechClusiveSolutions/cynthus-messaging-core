"""Identity User Rejected signal message for the Cynthus project"""

from ....common import AuditIdentityUserRejectedSignal, SignalMessage
from ..payload import IdentityUserRejectedPayload


class IdentityUserRejectedMessage(SignalMessage[IdentityUserRejectedPayload]):
    """
        Represents an identity user rejected signal message

        Emitted by: `cynthus-auth` when a sign-in is refused.
        Functional Purpose: Lets `cynthus-audit` and security monitoring see failed sign-ins. The password is never included.
    """

    event_type: str = AuditIdentityUserRejectedSignal.name
