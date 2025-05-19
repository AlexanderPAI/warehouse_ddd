from typing import List

from fastapi import APIRouter, Body

router = APIRouter(
    prefix="/order",
    tags=["Order"],
)


@router.post(path="/", summary="Create order")
async def create_order(
    products: List[int] | List[str] = Body(..., title="Product IDs")
):
    """Create order"""
    pass


@router.get(path="/", summary="Get order by ID")
async def get_order(order_id: int = Body(..., title="Order ID")):
    """Get order by ID"""
    pass
