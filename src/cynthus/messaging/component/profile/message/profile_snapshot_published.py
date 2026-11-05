"""ProfileSnapshotPublished signal message for the Cynthus project"""

from ....common import PublicProfileSnapshotPublishedSignal, SignalMessage
from ..payload import ProfileSnapshotPublishedPayload


class ProfileSnapshotPublishedMessage(SignalMessage[ProfileSnapshotPublishedPayload]):
    """
        Represents a public.profile.snapshot.published signal message

        Emitted by: `cynthus-profile` when a user signs in and has a profile.
        Functional Purpose: Pushes the profile (allergies, likes, dislikes, favorites, conditions) to the Analysis engine, which correlates it with shopping and inventory patterns to refine meal suggestions.
    """

    event_type: str = PublicProfileSnapshotPublishedSignal.name
