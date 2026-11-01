"""Signal Topic base class for the Cynthus project"""

from pydantic import BaseModel


class SignalTopic(BaseModel):
    """Represents one Azure Service Bus topic of the three-topic layout (ADD v6, section 5.1)."""

    name: str
