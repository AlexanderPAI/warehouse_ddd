from domain.dtos import (
    ProductDTO,  # OrderDTO # dataclass для order вообще не нужен в итоге
)


class WarehouseService:
    def __init__(
        self,
        uow,
        customer_model,
        product_model,
        order_model,
    ):
        self.uow = uow
        self.customer_model = customer_model
        self.product_model = product_model
        self.order_model = order_model

    async def create_customer(self):
        customer = self.customer_model()
        await self.uow.get_repository(self.customer_model).add(customer)
        return customer

    async def create_product(self, product: ProductDTO):
        product = self.product_model(
            name=product.name, quantity=product.quantity, price=product.price
        )
        await self.uow.get_repository(self.product_model).add(product)
        return product

    async def create_order(self, products):
        order = self.order_model(products=products)
        await self.uow.get_repository(self.order_model).add(order)
        return order
