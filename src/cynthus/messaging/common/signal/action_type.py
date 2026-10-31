"""Signal Action Type class for the Cynthus project"""

from enum import Enum


class SignalActionType(str, Enum):
    """Standardized signal action mutations"""

    ACCEPTED: str = 'accepted'
    ASSOCIATED: str = 'associated'
    AUTO_RESOLVED: str = 'auto_resolved'
    CAST: str = 'cast'
    CREATED: str = 'created'
    DELETED: str = 'deleted'
    GENERATED: str = 'generated'
    INITIATED: str = 'initiated'
    REJECTED: str = 'rejected'
    REQUESTED: str = 'requested'
    RESOLVED: str = 'resolved'
    UPDATED: str = 'updated'
