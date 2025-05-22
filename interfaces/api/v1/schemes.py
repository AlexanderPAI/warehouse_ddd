from pydantic import BaseModel, ConfigDict


class ProductResponseModel(BaseModel):
    id: int
    name: str
    quantity: int
    price: float

    model_config = ConfigDict(from_attributes=True)
