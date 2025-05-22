import asyncio
import logging

import uvicorn

from domain.dtos import ProductDTO
from domain.services import WarehouseService
from infrastructure.database import create_tables, session_factory
from infrastructure.models import Customer, Order, Product
from infrastructure.unit_of_work import SqlAlchemyUnitOfWork
from interfaces.api.api import app
from interfaces.repositories.base import BaseRepository

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


async def main():
    await create_tables()
    config = uvicorn.Config(app=app, host="0.0.0.0", port=8080)
    server = uvicorn.Server(config)
    await server.serve()


async def sec_main():
    await create_tables()
    uow = SqlAlchemyUnitOfWork(session_factory=session_factory)

    warehouse_service = WarehouseService(
        uow, customer_model=Customer, product_model=Product, order_model=Order
    )
    async with uow:
        uow.register_repository(Product, BaseRepository)
        uow.register_repository(Order, BaseRepository)
        uow.register_repository(Customer, BaseRepository)
        product1 = await warehouse_service.create_product(
            ProductDTO(name="apple", quantity=1, price=100)
        )
        product2 = await warehouse_service.create_product(
            ProductDTO(name="banana", quantity=1, price=100)
        )
        products = [product1, product2]
        order = await warehouse_service.create_order(products=products)
        new_customer = await warehouse_service.create_customer()
        logger.info(order.id)
        logger.info(new_customer.id)
        # uow.commit()
        # todo add some actions


if __name__ == "__main__":
    # main()
    asyncio.run(main())
