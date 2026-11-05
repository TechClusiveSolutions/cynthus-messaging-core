"""Public Profile Profile Requested signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_profile_profile_base import PublicProfileProfileSignalBase


class PublicProfileProfileRequestedSignal(PublicProfileProfileSignalBase):
    """Concrete signal: public.profile.profile.requested"""

    action = SignalActionType.REQUESTED
