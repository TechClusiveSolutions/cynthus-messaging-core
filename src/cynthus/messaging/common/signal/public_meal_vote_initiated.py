"""Public Meal Vote Initiated signal class for the Cynthus project"""

from .action_type import SignalActionType
from .public_meal_vote_base import PublicMealVoteSignalBase


class PublicMealVoteInitiatedSignal(PublicMealVoteSignalBase):
    """Concrete signal: public.meal.vote.initiated"""

    action = SignalActionType.INITIATED
