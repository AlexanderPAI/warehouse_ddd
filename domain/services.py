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
        obj = await self.uow.get_repository(self.customer_model).add(customer)
        return obj

    async def get_customer(self, customer_id: int):
        obj = await self.uow.get_repository(self.customer_model).get(obj_id=customer_id)
        return obj

    async def create_product(self, product: ProductDTO):
        product = self.product_model(
            name=product.name, quantity=product.quantity, price=product.price
        )
        obj = await self.uow.get_repository(self.product_model).add(product)
        return obj

    async def get_product(self, product_id: int):
        obj = await self.uow.get_repository(self.product_model).get(obj_id=product_id)
        return obj

    async def create_order(self, products):
        order = self.order_model(products=products)
        obj = await self.uow.get_repository(self.order_model).add(order)
        return obj
