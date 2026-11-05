"""What came of a request: the status and result to answer with, and the facts to publish."""

from dataclasses import dataclass, field
from typing import Any

from .fact import Fact


@dataclass
class Outcome:
    status: int
    result: Any = None
    error: str | None = None
    facts: list[Fact] = field(default_factory=list)
