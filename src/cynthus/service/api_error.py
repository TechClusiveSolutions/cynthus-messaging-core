"""The error raised for a request that cannot be carried out."""

from pydantic import ValidationError


class ApiError(Exception):
    """404 for something that does not exist (or belongs to another workspace), 409 for a conflict, 422 for bad input."""

    def __init__(self, status_code: int, message: str) -> None:
        super().__init__(message)

        self.status_code = status_code
        self.message = message

    @classmethod
    def invalid(cls, error: ValidationError) -> 'ApiError':
        """A request the service cannot accept is described by its first problem."""

        first = error.errors()[0]
        where = '.'.join(str(part) for part in first['loc'])

        return cls(422, f'{where}: {first["msg"]}' if where else first['msg'])
