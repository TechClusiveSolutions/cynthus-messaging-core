"""Public Meal Vote Auto Resolved signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_meal_vote_base import PublicMealVoteSignalBase


class PublicMealVoteAutoResolvedSignal(PublicMealVoteSignalBase):
    """Concrete signal: public.meal.vote.auto_resolved"""

    action = SignalActionType.AUTO_RESOLVED
