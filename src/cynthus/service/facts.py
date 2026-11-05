"""Publishes the public facts that follow a successful change, for the Cynthus project"""

from uuid import uuid4

from cynthus.core import logging
from cynthus.security import TokenClaims

from .fact import Fact

LOGGER = logging.getLogger(__name__)


class Facts:
    """Facts are published after the change is committed; a bus failure is logged and does not undo the change."""

    @staticmethod
    async def publish(publisher, claims: TokenClaims, fact: Fact) -> None:
        message = fact.message_class(
            lifecycle_action=fact.lifecycle,
            correlation_id=uuid4(),
            organization_id=claims.organization_id,
            workspace_id=claims.workspace_id,
            actor_id=claims.subject,
            payload=fact.payload,
        )

        try:
            await publisher.publish(message)
        except Exception:
            LOGGER.getChild('publish').exception('Could not publish %s', message.event_type)
