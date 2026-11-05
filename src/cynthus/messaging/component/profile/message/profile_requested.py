"""ProfileRequested signal message for the Cynthus project"""

from ....common import PublicProfileProfileRequestedSignal, SignalMessage
from ..payload import ProfileRequestedPayload


class ProfileRequestedMessage(SignalMessage[ProfileRequestedPayload]):
    """
        Represents a public.profile.profile.requested signal message

        Emitted by: `cynthus-core-api` when a caller asks to create, get, update or delete their profile.
        Functional Purpose: Hands the request to the Profile service so the caller gets an immediate acknowledgement.
    """

    event_type: str = PublicProfileProfileRequestedSignal.name
