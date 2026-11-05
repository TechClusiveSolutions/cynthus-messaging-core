"""ProfileUpdated signal message for the Cynthus project"""

from ....common import PublicProfileProfileUpdatedSignal, SignalMessage
from ..payload import ProfileUpdatedPayload


class ProfileUpdatedMessage(SignalMessage[ProfileUpdatedPayload]):
    """
        Represents a public.profile.profile.updated signal message

        Emitted by: `cynthus-profile` when a profile is changed.
        Functional Purpose: Lets other services know which parts of a profile changed, without the contents.
    """

    event_type: str = PublicProfileProfileUpdatedSignal.name
