"""Public Meal Vote Cast signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_meal_vote_base import PublicMealVoteSignalBase


class PublicMealVoteCastSignal(PublicMealVoteSignalBase):
    """Concrete signal: public.meal.vote.cast"""

    action = SignalActionType.CAST
