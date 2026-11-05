"""Hook that lets a service record the access decisions made by `RequirePermission`."""

from .token_claims import TokenClaims


class AccessRecorder:
    """Does nothing. A service subclasses it to publish the audit signals and stores it on `app.state.access_recorder`.

    A recorder that raises never changes the outcome of a request; the failure is logged and the decision stands.
    """

    async def granted(self, claims: TokenClaims, permission: str, resource: str, method: str) -> None:
        """The token is valid and grants `permission`."""

    async def rejected(self, reason: str, resource: str, method: str) -> None:
        """There is no valid token (HTTP 401)."""

    async def denied(self, claims: TokenClaims, permission: str, resource: str, method: str) -> None:
        """The token is valid but does not grant `permission` (HTTP 403)."""
