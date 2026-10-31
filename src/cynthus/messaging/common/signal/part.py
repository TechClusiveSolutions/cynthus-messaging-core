"""Signal Part class for the Cynthus project"""

from pydantic import BaseModel

from .model_config import create_model_config


class SignalPart(BaseModel):
    """Represents a part of a signal message"""

    model_config = create_model_config(frozen=True)
