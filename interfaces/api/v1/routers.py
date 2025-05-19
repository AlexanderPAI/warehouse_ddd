from fastapi import APIRouter

from interfaces.api.v1.endpoints import customer, order, product

router = APIRouter(prefix="/v1")

router.include_router(customer.router)
router.include_router(order.router)
router.include_router(product.router)
