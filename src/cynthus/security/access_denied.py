"""The error raised when a request is not authenticated or not permitted."""

from fastapi import Request
from fastapi.responses import JSONResponse


class AccessDenied(Exception):
    """401 when the token is missing or not trusted, 403 when it lacks the permission the route needs."""

    def __init__(self, status_code: int, reason: str) -> None:
        super().__init__(reason)

        self.status_code = status_code
        self.reason = reason


async def access_denied_handler(request: Request, error: AccessDenied) -> JSONResponse:
    """Answers with the single error envelope from the engineering standards."""

    headers = {'WWW-Authenticate': 'Bearer'} if error.status_code == 401 else None

    return JSONResponse({'error': error.reason}, status_code=error.status_code, headers=headers)
