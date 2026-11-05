"""Public Profile Profile Created signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_profile_profile_base import PublicProfileProfileSignalBase


class PublicProfileProfileCreatedSignal(PublicProfileProfileSignalBase):
    """Concrete signal: public.profile.profile.created"""

    action = SignalActionType.CREATED
