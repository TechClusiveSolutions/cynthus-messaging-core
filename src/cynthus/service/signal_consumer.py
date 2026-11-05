"""Signal consumer for the Cynthus project"""

import asyncio

from cynthus.core import logging
from cynthus.messaging.topic import CoreSignalTopic

LOGGER = logging.getLogger(__name__)


class SignalConsumer:
    """Receives the signals of one subscription and hands each to a handler, until it is cancelled.

    A message the handler accepts is completed. A message the handler raises on is dead-lettered, so it can be looked at
    later without blocking the messages behind it. Cancelling the task running `run()` stops the loop without settling
    the message in hand; the broker redelivers it.
    """

    def __init__(self, client, subscription_name: str, handler, topic_name: str | None = None) -> None:
        self._client = client
        self._subscription_name = subscription_name
        self._handler = handler
        self._topic_name = topic_name or CoreSignalTopic().name

    async def run(self) -> None:
        logger = LOGGER.getChild('run')

        receiver = self._client.get_subscription_receiver(
            topic_name=self._topic_name,
            subscription_name=self._subscription_name,
        )

        async with receiver:
            async for message in receiver:
                try:
                    await self._handler(message)
                except asyncio.CancelledError:
                    raise
                except Exception:
                    logger.exception(
                        'Failed to process a signal; dead-lettering message %s', getattr(message, 'message_id', None)
                    )

                    await receiver.dead_letter_message(message, reason='processing_failed')
                else:
                    await receiver.complete_message(message)
