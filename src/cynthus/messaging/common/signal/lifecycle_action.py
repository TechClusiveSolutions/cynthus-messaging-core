"""Lifecycle action class for the Cynthus project"""

from enum import Enum


class LifecycleAction(str, Enum):
    """Standardized entity state mutations to prevent event type explosion."""

    CREATED: str = "created"
    UPDATED: str = "updated"
    DELETED: str = "deleted"
    SNAPSHOT: str = "snapshot"
