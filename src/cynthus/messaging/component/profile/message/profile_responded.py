"""ProfileResponded signal message for the Cynthus project"""

from ....common import PublicProfileProfileRespondedSignal, SignalMessage
from ..payload import ProfileRespondedPayload


class ProfileRespondedMessage(SignalMessage[ProfileRespondedPayload]):
    """
        Represents a public.profile.profile.responded signal message

        Emitted by: `cynthus-profile` when it has dealt with a profile request.
        Functional Purpose: Carries the outcome back to `cynthus-core-api`, which relays it to the caller.
    """

    event_type: str = PublicProfileProfileRespondedSignal.name
