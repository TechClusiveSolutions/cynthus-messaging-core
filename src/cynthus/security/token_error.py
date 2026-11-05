"""Token error for the Cynthus project"""


class TokenError(Exception):
    """Raised when an access token is missing, malformed, expired, or not trusted."""

    def __init__(self, reason: str) -> None:
        super().__init__(reason)

        self.reason = reason
