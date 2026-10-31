"""Public Meal Vote Resolved signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_meal_vote_base import PublicMealVoteSignalBase


class PublicMealVoteResolvedSignal(PublicMealVoteSignalBase):
    """Concrete signal: public.meal.vote.resolved"""

    action = SignalActionType.RESOLVED
