"""Public Profile Profile Signal Base class for the Cynthus project"""

from .public_profile_base import PublicProfileSignalBase


class PublicProfileProfileSignalBase(PublicProfileSignalBase, abstract=True):
    """Intermediate base for all public profile profile signals. Sets the aggregate component."""

    aggregate = 'profile'
