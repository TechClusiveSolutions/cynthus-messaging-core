"""Signal Message class for the Cynthus project"""

from typing import Generic, TypeVar

from .message_base import SignalMessageBase
from .payload import SignalPayload

PayloadT = TypeVar('PayloadT', bound=SignalPayload, default=SignalPayload)


class SignalMessage(SignalMessageBase, Generic[PayloadT]):
    """The immutable common spine published to cynthus-events-topic."""

    payload: PayloadT
