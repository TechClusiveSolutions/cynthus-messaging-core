"""Reads the identifiers a request carries."""

import uuid

from .api_error import ApiError


class Identifier:
    """A malformed identifier is a 422, not a crash."""

    @staticmethod
    def parse(value, name: str) -> uuid.UUID:
        if value is None or value == '':
            raise ApiError(422, f'{name}: is required')

        try:
            return value if isinstance(value, uuid.UUID) else uuid.UUID(str(value))
        except ValueError as error:
            raise ApiError(422, f'{name}: is not a valid identifier') from error

    @classmethod
    def optional(cls, value, name: str) -> uuid.UUID | None:
        return None if value in (None, '') else cls.parse(value, name)
