"""ProfileDeleted signal message for the Cynthus project"""

from ....common import PublicProfileProfileDeletedSignal, SignalMessage
from ..payload import ProfileDeletedPayload


class ProfileDeletedMessage(SignalMessage[ProfileDeletedPayload]):
    """
        Represents a public.profile.profile.deleted signal message

        Emitted by: `cynthus-profile` when a profile is deleted.
        Functional Purpose: Lets other services drop what they hold for the profile.
    """

    event_type: str = PublicProfileProfileDeletedSignal.name
