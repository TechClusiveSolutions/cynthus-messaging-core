"""Builds the SQLAlchemy URL of a service's database from the service environment."""

from collections.abc import Mapping
from os import environ

from sqlalchemy import URL

DRIVER = 'postgresql+psycopg'


class DatabaseUrl:
    """Reads DB_HOST, DB_PORT, DB_NAME, DB_USERNAME and DB_PASSWORD (DB_DRIVER names the image, not the dialect)."""

    def __init__(self, environment: Mapping[str, str] | None = None) -> None:
        self._environment = environ if environment is None else environment

    def build(self) -> URL:
        values = self._environment

        return URL.create(
            DRIVER,
            username=values.get('DB_USERNAME'),
            password=values.get('DB_PASSWORD'),
            host=values.get('DB_HOST', 'db'),
            port=int(values.get('DB_PORT', '5432')),
            database=values.get('DB_NAME'),
        )
