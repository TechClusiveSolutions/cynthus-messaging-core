"""Identity User Authenticated signal message for the Cynthus project"""

from ....common import AuditIdentityUserAuthenticatedSignal, SignalMessage
from ..payload import IdentityUserAuthenticatedPayload


class IdentityUserAuthenticatedMessage(SignalMessage[IdentityUserAuthenticatedPayload]):
    """
        Represents an identity user authenticated signal message

        Emitted by: `cynthus-auth` when a user signs in with correct credentials.
        Functional Purpose: Records the sign-in for `cynthus-audit`.
    """

    event_type: str = AuditIdentityUserAuthenticatedSignal.name
