from typing import Any, Dict, List


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

    async def create_product(self, product: Dict[Any, Any]):
        product = self.product_model(**product)
        obj = await self.uow.get_repository(self.product_model).add(product)
        return obj

    async def get_product(self, product_id: int):
        obj = await self.uow.get_repository(self.product_model).get(obj_id=product_id)
        return obj

    async def create_order(
        self,
        customer_id: int,
        products_ids: List[int],
    ):
        order = self.order_model()
        products = await self.uow.get_repository(self.product_model).list(
            self.product_model.id.in_(products_ids)
        )
        obj = await self.uow.get_repository(self.order_model).add(order)
        customer = await self.uow.get_repository(self.customer_model).get(
            obj_id=customer_id
        )
        obj.products = products
        customer.orders.append(obj)
        return obj
