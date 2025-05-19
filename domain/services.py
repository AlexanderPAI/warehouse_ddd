from typing import List

from .models import Order, Product


class WarehouseService:
    def __init__(
        self,
        uow,
        product_orm,
        order_orm,
    ):
        self.uow = uow
        self.product_orm = product_orm
        self.order_orm = order_orm

    async def create_product(self, name: str, quantity: int, price: float) -> Product:
        product = Product(name=name, quantity=quantity, price=price)
        await self.uow.get_repository(self.product_orm).add(product.as_dict())
        return product

    async def create_order(self, products: List[Product]) -> Order:
        order = Order(products=products)
        await self.uow.get_repository(self.order_orm).add(order.as_dict())
        return order
