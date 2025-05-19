import logging
from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

logger = logging.getLogger(__name__)


class UnitOfWork(ABC):
    @abstractmethod
    async def __aenter__(self):
        pass

    @abstractmethod
    async def __aexit__(self, exception_type, exception_value, traceback):
        pass

    @abstractmethod
    async def commit(self):
        pass

    @abstractmethod
    async def rollback(self):
        pass


class SqlAlchemyUnitOfWork(UnitOfWork):

    def __init__(self, session_factory) -> None:
        self.session_factory = session_factory
        self._session: AsyncSession | None = None
        self._repositories = {}

    async def __aenter__(self):
        self._session = self.session_factory()
        try:
            await self.commit()
            return self
        except Exception as e:
            await self._session.rollback()
            logger.error(e)

    async def __aexit__(self, exception_type, exception_value, traceback):
        if self._session is not None:
            try:
                if exception_type is None:
                    await self.commit()
                else:
                    await self.rollback()
                    logger.error("Is rollback")
            finally:
                await self._session.close()

    async def commit(self) -> None:
        if self._session is not None:
            await self._session.commit()

    async def rollback(self) -> None:
        if self._session is not None:
            await self._session.rollback()

    def register_repository(self, model, repository) -> None:
        if self._session is None:
            raise RuntimeError("Session is not initialized")
        self._repositories[model] = repository(session=self._session, model=model)

    def get_repository(self, orm_type):
        return self._repositories[orm_type]
