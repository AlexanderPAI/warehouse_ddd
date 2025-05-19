import asyncio
import logging

from domain.dtos import ProductDTO
from domain.services import WarehouseService
from infrastructure.database import create_tables, session_factory
from infrastructure.models import Order, Product
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

    warehouse_service = WarehouseService(uow, product_model=Product, order_model=Order)
    async with uow:
        uow.register_repository(Product, BaseRepository)
        uow.register_repository(Order, BaseRepository)
        product1 = await warehouse_service.create_product(
            ProductDTO(name="apple", quantity=1, price=100)
        )
        product2 = await warehouse_service.create_product(
            ProductDTO(name="banana", quantity=1, price=100)
        )
        products = [product1, product2]
        order = await warehouse_service.create_order(products=products)
        logger.info(order)
        # uow.commit()
        # todo add some actions


if __name__ == "__main__":
    asyncio.run(main())
