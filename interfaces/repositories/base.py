from typing import Any, Dict, Generic, Sequence, Type, TypeVar

from sqlalchemy import select

# from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from interfaces.repositories.abstract import AbstractRepository

OrmType = TypeVar("OrmType")


class BaseRepository(AbstractRepository, Generic[OrmType,]):

    def __init__(
        self,
        orm: Type[OrmType],
        session: AsyncSession,
    ) -> None:
        self._orm = orm
        self._session = session

    async def add(self, data_obj: Dict[Any, Any]) -> None:
        """
        Add to DB.
        :param data_obj: Dict[Any, Any]
        :return: None
        """
        obj = self._orm(**data_obj)
        self._session.add(obj)

    async def get(self, obj_id: int) -> Dict[Any, Any]:
        """
        Get from DB.
        :param obj_id: int
        :return: Dict[Any, Any]
        """
        query = select(self._orm).where(self._orm.id == obj_id)
        result = await self._session.execute(query)
        return result.scalars().one()

    async def list(self, *args, **kwargs) -> Sequence[OrmType]:
        """
        List from DB
        :return: List[Dict[Any, Any]]
        """
        obj_list = await self._session.execute(
            select(self._orm).filter(*args).filter_by(**kwargs)
        )
        return obj_list.scalars().all()
