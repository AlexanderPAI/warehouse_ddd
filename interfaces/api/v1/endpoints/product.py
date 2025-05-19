from typing import Optional

from fastapi import APIRouter, Body

router = APIRouter(
    prefix="/product",
    tags=["Product"],
)


@router.post(path="/", summary="Create product")
async def create_product(
    name: str = Body(..., title="Name"),
    quantity: int = Body(..., title="Quantity"),
    price: float = Body(..., title="Price"),
):
    """Create product"""
    pass


@router.get(path="/", summary="Get product by ID")
async def get_product(
    name: Optional[str] = Body(None, title="Name"),
    product_id: Optional[int] = Body(None, title="product_id"),
):
    """Get product by ID"""
    pass
