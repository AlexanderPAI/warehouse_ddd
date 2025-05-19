import asyncio
import logging

from domain.services import WarehouseService
from infrastructure.database import create_tables, session_factory
from infrastructure.orm import OrderORM, ProductORM
from infrastructure.unit_of_work import SqlAlchemyUnitOfWork
from interfaces.repositories.base import BaseRepository

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


async def main():
    await create_tables()
    uow = SqlAlchemyUnitOfWork(session_factory=session_factory)

    warehouse_service = WarehouseService(
        uow, product_orm=ProductORM, order_orm=OrderORM
    )
    async with uow:
        uow.register_repository(ProductORM, BaseRepository)
        uow.register_repository(OrderORM, BaseRepository)
        new_product = await warehouse_service.create_product(
            name="test1", quantity=1, price=100
        )
        logger.info(f"create product: {new_product}")
        # uow.commit()
        # todo add some actions


if __name__ == "__main__":
    asyncio.run(main())
