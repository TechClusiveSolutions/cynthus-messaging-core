"""Decision Reason class for the Cynthus project"""

from enum import Enum


class DecisionReason(str, Enum):
    NOT_ENOUGH_ENERGY: str = 'not_enough_energy'
    NOT_ENOUGH_TIME: str = 'not_enough_time'
    DISLIKE_INGREDIENT: str = 'dislike_ingredient'
    ALLERGIC_TO_INGREDIENT: str = 'allergic_to_ingredient'
    JUST_BECAUSE: str = 'just_because'
    NOT_SPECIFIED: str = 'not_specified'
    NOT_FEELING_WELL: str = 'not_feeling_well'
    LIKE_IT: str = 'like_it'
    LOVE_IT: str = 'love_it'
    SOUNDS_YUMMY: str = 'sounds_yummy'
    SOUNDS_GROSS: str = 'sounds_gross'
    FOND_MEMORIES: str = 'fond_memories'
    FEELING_ADVENTUROUS: str = 'feeling_adventurous'
