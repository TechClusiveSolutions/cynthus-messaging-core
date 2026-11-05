"""The error raised when a genuine token does not grant the permission a request needs."""

from cynthus.security import TokenError


class Forbidden(TokenError):
    """A TokenError that means 403 rather than 401: the caller is known but not allowed."""
