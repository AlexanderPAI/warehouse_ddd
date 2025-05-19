from typing import List

from interfaces.repositories.abstract import AbstractRepository

from .models import Order, Product


class WarehouseService:
    def __init__(
        self, product_repo: AbstractRepository, order_repo: AbstractRepository
    ):
        self.product_repo = product_repo
        self.order_repo = order_repo

    def create_product(self, name: str, quantity: int, price: float) -> Product:
        product = Product(id=1, name=name, quantity=quantity, price=price)
        self.product_repo.add(product.as_dict())
        return product

    def create_order(self, products: List[Product]) -> Order:
        order = Order(id=1, products=products)
        self.order_repo.add(order.as_dict())
        return order
