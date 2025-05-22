from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class ProductResponseModel(BaseModel):
    id: int
    name: str
    quantity: int
    price: float

    model_config = ConfigDict(from_attributes=True)


class OrderResponseModel(BaseModel):
    id: int
    products: Optional[List[ProductResponseModel]] = None

    model_config = ConfigDict(from_attributes=True)


class CustomerResponseModel(BaseModel):
    id: int
    orders: Optional[List[OrderResponseModel]] = None

    model_config = ConfigDict(from_attributes=True)
