"""Public Profile Profile Responded signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_profile_profile_base import PublicProfileProfileSignalBase


class PublicProfileProfileRespondedSignal(PublicProfileProfileSignalBase):
    """Concrete signal: public.profile.profile.responded"""

    action = SignalActionType.RESPONDED
