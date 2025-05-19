from typing import List, Optional

from fastapi import APIRouter, Body

router = APIRouter()


@router.get(path="/")
async def root():
    return {"Hello: World"}


@router.post(path="/create_customer")
async def create_customer():
    pass


@router.get(path="/get_customer")
async def get_customer(customer_id: int = Body(title="Customer ID")):
    pass


@router.post(path="/create_product")
async def create_product(
    name: str = Body(..., title="Name"),
    quantity: int = Body(..., title="Quantity"),
    price: float = Body(..., title="Price"),
):
    pass


@router.get(path="/get_product")
async def get_product(
    name: Optional[str] = Body(None, title="Name"),
    product_id: Optional[int] = Body(None, title="product_id"),
):
    pass


@router.post(path="/create_order")
async def create_order(
    products: List[int] | List[str] = Body(..., title="Product IDs")
):
    pass


@router.get(path="/get_order")
async def get_order(order_id: int = Body(..., title="Order ID")):
    pass
