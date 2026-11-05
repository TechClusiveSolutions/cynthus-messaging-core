"""Signal Action Type class for the Cynthus project"""

from enum import Enum


class SignalActionType(str, Enum):
    """Standardized signal action mutations"""

    ACCEPTED: str = 'accepted'
    ADDED: str = 'added'
    ASSOCIATED: str = 'associated'
    AUTHENTICATED: str = 'authenticated'
    AUTO_RESOLVED: str = 'auto_resolved'
    CAST: str = 'cast'
    CREATED: str = 'created'
    DELETED: str = 'deleted'
    DENIED: str = 'denied'
    GENERATED: str = 'generated'
    GRANTED: str = 'granted'
    INITIATED: str = 'initiated'
    ISSUED: str = 'issued'
    REJECTED: str = 'rejected'
    REMOVED: str = 'removed'
    REQUESTED: str = 'requested'
    RESOLVED: str = 'resolved'
    RESPONDED: str = 'responded'
    UPDATED: str = 'updated'
