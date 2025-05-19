from typing import Any, Dict, Generic, Sequence, Type, TypeVar

from sqlalchemy import select

# from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from interfaces.repositories.abstract import AbstractRepository

ModelType = TypeVar("ModelType")


class BaseRepository(AbstractRepository, Generic[ModelType,]):

    def __init__(
        self,
        model: Type[ModelType],
        session: AsyncSession,
    ) -> None:
        self._model = model
        self._session = session

    async def add(self, data_obj: Dict[Any, Any] | Any) -> None:
        """
        Add to DB.
        :param data_obj: Dict[Any, Any]
        :return: None
        """
        if isinstance(data_obj, Dict):
            obj = self._model(**data_obj)
        else:
            obj = data_obj
        self._session.add(obj)
        return obj

    async def get(self, obj_id: int) -> Dict[Any, Any]:
        """
        Get from DB.
        :param obj_id: int
        :return: Dict[Any, Any]
        """
        query = select(self._model).where(self._model.id == obj_id)
        result = await self._session.execute(query)
        return result.scalars().one()

    async def list(self, *args, **kwargs) -> Sequence[ModelType]:
        """
        List from DB
        :return: List[Dict[Any, Any]]
        """
        obj_list = await self._session.execute(
            select(self._model).filter(*args).filter_by(**kwargs)
        )
        return obj_list.scalars().all()
