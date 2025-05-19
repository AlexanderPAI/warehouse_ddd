import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from domain.services import WarehouseService
from infrastructure.database import DATABASE_URL
from infrastructure.orm import Base, OrderORM, ProductORM
from infrastructure.unit_of_work import SqlAlchemyUnitOfWork
from interfaces.repositories.base import BaseRepository

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


engine = create_engine(DATABASE_URL)
SessionFactory = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


def main():

    uow = SqlAlchemyUnitOfWork(session_factory=SessionFactory)

    warehouse_service = WarehouseService(
        uow, product_orm=ProductORM, order_orm=OrderORM
    )
    with uow:
        uow.register_repository(ProductORM, BaseRepository)
        uow.register_repository(OrderORM, BaseRepository)
        new_product = warehouse_service.create_product(
            name="test1", quantity=1, price=100
        )
        logger.info(f"create product: {new_product}")
        uow.commit()
        # todo add some actions


if __name__ == "__main__":
    main()
