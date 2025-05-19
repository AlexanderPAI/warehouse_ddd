import logging
from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


class UnitOfWork(ABC):
    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, exception_type, exception_value, traceback):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass


class SqlAlchemyUnitOfWork(UnitOfWork):

    def __init__(self, session_factory) -> None:
        self.session_factory = session_factory
        self._session: Session | None = None
        self._repositories = {}

    def __enter__(self):
        self._session = self.session_factory()
        try:
            self.commit()
            return self
        except Exception as e:
            self._session.rollback()
            logger.error(e)

    def __exit__(self, exception_type, exception_value, traceback):
        if self._session is not None:
            if exception_type is not None:
                self.rollback()
                logger.error("Is rollback")
            self._session.close()

    def commit(self) -> None:
        if self._session is not None:
            self._session.commit()

    def rollback(self) -> None:
        if self._session is not None:
            self._session.rollback()

    def register_repository(self, orm_type, repository) -> None:
        if self._session is None:
            raise RuntimeError("Session is not initialized")
        self._repositories[orm_type] = repository(session=self._session, orm=orm_type)

    def get_repository(self, orm_type):
        return self._repositories[orm_type]
