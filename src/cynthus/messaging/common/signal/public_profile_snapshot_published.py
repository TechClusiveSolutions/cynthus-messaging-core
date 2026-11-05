"""Public Profile Snapshot Published signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_profile_snapshot_base import PublicProfileSnapshotSignalBase


class PublicProfileSnapshotPublishedSignal(PublicProfileSnapshotSignalBase):
    """Concrete signal: public.profile.snapshot.published"""

    action = SignalActionType.PUBLISHED
