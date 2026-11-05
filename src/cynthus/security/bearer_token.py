"""Bearer token parsing for the Cynthus project"""

from .token_error import TokenError


class BearerToken:
    """Pulls the token out of an `Authorization: Bearer <token>` header value"""

    SCHEME = 'bearer'

    @classmethod
    def extract(cls, header: str | bytes | None) -> str:
        if isinstance(header, bytes):
            header = header.decode('utf-8', errors='replace')

        if not header:
            raise TokenError('missing bearer token')

        scheme, _, token = header.strip().partition(' ')

        if scheme.lower() != cls.SCHEME or not token.strip():
            raise TokenError('malformed authorization header')

        return token.strip()
