"""Public Profile Snapshot Signal Base class for the Cynthus project"""

from .public_profile_base import PublicProfileSignalBase


class PublicProfileSnapshotSignalBase(PublicProfileSignalBase, abstract=True):
    """Intermediate base for all public profile snapshot signals. Sets the aggregate component."""

    aggregate = 'snapshot'
