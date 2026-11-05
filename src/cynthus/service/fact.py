"""A public fact that follows a successful change, for the Cynthus project"""

from dataclasses import dataclass
from typing import Any

from cynthus.messaging.common import LifecycleAction


@dataclass(frozen=True)
class Fact:
    """The message class, lifecycle and payload of a signal such as public.inventory.location.created or public.profile.profile.updated."""

    message_class: type
    lifecycle: LifecycleAction
    payload: Any
