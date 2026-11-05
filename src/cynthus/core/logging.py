"""Logging configuration for the Cynthus project

Import this module where the standard library's `logging` would be imported:

    from cynthus.core import logging

    LOGGER = logging.getLogger(__name__)

The first call to `getLogger` applies the common configuration (`configure`). The `LOG_LEVEL` and `LOG_FORMAT`
environment variables override the defaults; arguments to `configure` override both.
"""

import logging as stdlib
from os import environ

CRITICAL = stdlib.CRITICAL
ERROR = stdlib.ERROR
WARNING = stdlib.WARNING
INFO = stdlib.INFO
DEBUG = stdlib.DEBUG

Logger = stdlib.Logger

DEFAULT_LEVEL = 'INFO'
DEFAULT_FORMAT = '%(asctime)s %(levelname)-8s %(name)s - %(message)s'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
DEFAULT_AZURE_LEVEL = 'WARNING'

__all__ = [
    'CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'Logger',
    'DEFAULT_LEVEL', 'DEFAULT_FORMAT', 'DEFAULT_DATE_FORMAT', 'DEFAULT_AZURE_LEVEL',
    'configure', 'getLogger',
]

_configured = False


def _resolve_level(level: int | str) -> int:
    if isinstance(level, int):
        return level

    text = level.strip().upper()

    if text.isdigit():
        return int(text)

    try:
        return stdlib.getLevelNamesMapping()[text]
    except KeyError:
        raise ValueError(f'Unknown log level: {level!r}') from None


def configure(
    level: int | str | None = None,
    format: str | None = None,
    datefmt: str | None = None,
    force: bool = False,
) -> None:
    """Apply the common logging configuration to the root logger.

    Like `logging.basicConfig`, this does nothing when the root logger already has handlers unless `force` is set.
    """

    global _configured

    resolved = _resolve_level(level if level is not None else environ.get('LOG_LEVEL') or DEFAULT_LEVEL)

    stdlib.basicConfig(
        level=resolved,
        format=format or environ.get('LOG_FORMAT') or DEFAULT_FORMAT,
        datefmt=datefmt or DEFAULT_DATE_FORMAT,
        force=force,
    )

    # The Azure SDK logs every AMQP frame and HTTP exchange at INFO
    stdlib.getLogger('azure').setLevel(_resolve_level(environ.get('AZURE_LOG_LEVEL') or DEFAULT_AZURE_LEVEL))

    _configured = True


def getLogger(name: str | None = None) -> Logger:
    """Return the named logger, applying the common configuration first if that has not happened yet."""

    if not _configured:
        configure()

    return stdlib.getLogger(name)
