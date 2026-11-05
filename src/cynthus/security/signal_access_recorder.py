"""Access recorder that publishes the access decisions as audit signals."""

from uuid import UUID, uuid4

from cynthus.messaging.common import LifecycleAction
from cynthus.messaging.component.identity import (
    IdentityAccessDeniedMessage,
    IdentityAccessDeniedPayload,
    IdentityAccessGrantedMessage,
    IdentityAccessGrantedPayload,
    IdentityAccessRejectedMessage,
    IdentityAccessRejectedPayload,
)

from .access_recorder import AccessRecorder
from .token_claims import TokenClaims

# A request without a valid token has no known caller, so it has no tenant either
NOBODY = UUID(int=0)


class SignalAccessRecorder(AccessRecorder):
    """Publishes `audit.identity.access.granted`, `.rejected` and `.denied` with a `SignalPublisher`.

    Tokens are never put on a signal; a token is named by its id.
    """

    def __init__(self, publisher) -> None:
        self._publisher = publisher

    async def granted(self, claims: TokenClaims, permission: str, resource: str, method: str) -> None:
        await self._publisher.publish(IdentityAccessGrantedMessage(
            lifecycle_action=LifecycleAction.CREATED,
            payload=IdentityAccessGrantedPayload(
                user_id=str(claims.subject), token_id=claims.token_id, permission=permission,
                resource=resource, method=method,
            ),
            **self._caller(claims),
        ))

    async def rejected(self, reason: str, resource: str, method: str) -> None:
        await self._publisher.publish(IdentityAccessRejectedMessage(
            lifecycle_action=LifecycleAction.CREATED,
            payload=IdentityAccessRejectedPayload(reason=reason, resource=resource, method=method),
            correlation_id=uuid4(), organization_id=NOBODY, workspace_id=NOBODY, actor_id=NOBODY,
        ))

    async def denied(self, claims: TokenClaims, permission: str, resource: str, method: str) -> None:
        await self._publisher.publish(IdentityAccessDeniedMessage(
            lifecycle_action=LifecycleAction.CREATED,
            payload=IdentityAccessDeniedPayload(
                user_id=str(claims.subject), token_id=claims.token_id, required_permission=permission,
                granted_permissions=list(claims.permissions), roles=list(claims.roles),
                resource=resource, method=method,
            ),
            **self._caller(claims),
        ))

    @staticmethod
    def _caller(claims: TokenClaims) -> dict:
        return {
            'correlation_id': uuid4(), 'organization_id': claims.organization_id,
            'workspace_id': claims.workspace_id, 'actor_id': claims.subject,
        }
