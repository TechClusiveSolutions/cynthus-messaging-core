"""Signal Publisher interface for the Cynthus project"""

from abc import ABC, abstractmethod

from ..common.signal.message_base import SignalMessageBase
from ..topic.signal_topic import SignalTopic


class SignalPublisher(ABC):
    """
        Publishes signal messages to a topic

        Application code depends on this interface, never on a broker class (ADR-006).
    """

    @abstractmethod
    async def publish(self, topic: SignalTopic, message: SignalMessageBase) -> None:
        """Publish ``message`` to ``topic``. Must not return before the broker has accepted the message."""
