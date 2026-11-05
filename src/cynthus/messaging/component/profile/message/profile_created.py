"""ProfileCreated signal message for the Cynthus project"""

from ....common import PublicProfileProfileCreatedSignal, SignalMessage
from ..payload import ProfileCreatedPayload


class ProfileCreatedMessage(SignalMessage[ProfileCreatedPayload]):
    """
        Represents a public.profile.profile.created signal message

        Emitted by: `cynthus-profile` when a profile is created.
        Functional Purpose: Lets other services know a profile exists. It names which parts were set, not their contents.
    """

    event_type: str = PublicProfileProfileCreatedSignal.name
