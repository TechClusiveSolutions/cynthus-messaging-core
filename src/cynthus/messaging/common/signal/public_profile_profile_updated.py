"""Public Profile Profile Updated signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_profile_profile_base import PublicProfileProfileSignalBase


class PublicProfileProfileUpdatedSignal(PublicProfileProfileSignalBase):
    """Concrete signal: public.profile.profile.updated"""

    action = SignalActionType.UPDATED
