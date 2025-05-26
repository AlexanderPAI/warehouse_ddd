from abc import ABC
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class EntityDTO(ABC):
    def as_dict(self):
        return {
            key: value
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        }


@dataclass
class ProductDTO(EntityDTO):
    name: str
    quantity: int
    price: float
    id: Optional[int] = None


@dataclass
class OrderDTO(EntityDTO):
    id: Optional[int] = None
    products: Optional[List[ProductDTO]] = field(default_factory=list)

    def add_product(self, product: ProductDTO):
        self.products.append(product)

    def as_dict(self):
        dct = {}
        for key, value in self.__dict__.items():
            if isinstance(value, list):
                new_value = []
                for v in value:
                    new_value.append(v.as_dict())
                value = new_value
            dct[key] = value
        return dct


@dataclass
class CustomerDTO(EntityDTO):
    id: Optional[int] = None
    orders: Optional[List[OrderDTO]] = field(default_factory=list)

    def add_product(self, order: OrderDTO):
        self.orders.append(order)

    def as_dict(self):
        dct = {}
        for key, value in self.__dict__.items():
            if isinstance(value, list):
                new_value = []
                for v in value:
                    new_value.append(v.as_dict())
                value = new_value
            dct[key] = value
        return dct
