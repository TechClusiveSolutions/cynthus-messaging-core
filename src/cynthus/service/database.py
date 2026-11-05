"""Async access to a service's database for the Cynthus project"""

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from .database_url import DatabaseUrl


class Database:
    """Creates the engine on first use, so importing the service never needs a database."""

    def __init__(self, url=None) -> None:
        self._url = url
        self._engine: AsyncEngine | None = None
        self._sessions: async_sessionmaker[AsyncSession] | None = None

    def session(self) -> AsyncSession:
        if self._sessions is None:
            self._engine = create_async_engine(self._url or DatabaseUrl().build(), pool_pre_ping=True)
            self._sessions = async_sessionmaker(self._engine, expire_on_commit=False)

        return self._sessions()

    async def dispose(self) -> None:
        if self._engine is not None:
            await self._engine.dispose()

        self._engine = None
        self._sessions = None
