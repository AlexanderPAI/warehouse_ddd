from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from domain.services import WarehouseService
from infrastructure.database import DATABASE_URL
from infrastructure.orm import Base, OrderORM, ProductORM

# from interfaces.repositories import (
#     SqlAlchemyOrderRepository,
#     SqlAlchemyProductRepository,
# )
from infrastructure.unit_of_work import SqlAlchemyUnitOfWork
from interfaces.repositories.base import BaseRepository

engine = create_engine(DATABASE_URL)
SessionFactory = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


def main():
    session = SessionFactory()
    product_repo = BaseRepository(orm=ProductORM, session=session)
    order_repo = BaseRepository(orm=OrderORM, session=session)

    uow = SqlAlchemyUnitOfWork(session)

    warehouse_service = WarehouseService(product_repo, order_repo)
    with uow:
        new_product = warehouse_service.create_product(
            name="test1", quantity=1, price=100
        )
        uow.commit()
        print(f"create product: {new_product}")
        # todo add some actions


if __name__ == "__main__":
    main()
