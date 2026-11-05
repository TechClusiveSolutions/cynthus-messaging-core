"""Public Profile Profile Deleted signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_profile_profile_base import PublicProfileProfileSignalBase


class PublicProfileProfileDeletedSignal(PublicProfileProfileSignalBase):
    """Concrete signal: public.profile.profile.deleted"""

    action = SignalActionType.DELETED
