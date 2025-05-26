import logging
from typing import List

from fastapi import APIRouter, Body, HTTPException, Query

from domain.dtos import CustomerDTO, OrderDTO, ProductDTO
from domain.services import WarehouseService
from infrastructure.database import session_factory
from infrastructure.models import Customer, Order, Product
from infrastructure.unit_of_work import SqlAlchemyUnitOfWork
from interfaces.api.v1.schemes import (
    CustomerResponseModel,
    OrderResponseModel,
    ProductResponseModel,
)
from interfaces.repositories.base import BaseRepository

logger = logging.getLogger(__name__)

router = APIRouter()

uow = SqlAlchemyUnitOfWork(session_factory=session_factory)
warehouse_service = WarehouseService(
    uow, customer_model=Customer, product_model=Product, order_model=Order
)


@router.post(path="/customer", summary="Create customer", tags=["Customer"])
async def create_customer():
    """Create customer"""
    async with uow:
        uow.register_repository(Customer, BaseRepository)
        customer = await warehouse_service.create_customer()
        if not customer:
            raise HTTPException(
                status_code=500, detail=f"{Customer} could not be created"
            )
        return CustomerResponseModel.model_validate(customer, from_attributes=True)


@router.get(path="/customer", summary="Get customer by id or name", tags=["Customer"])
async def get_customer(customer_id: int = Query(..., title="Customer ID")):
    """Get customer by id or name"""
    async with uow:
        uow.register_repository(Customer, BaseRepository)
        customer = await warehouse_service.get_customer(customer_id)
        if not customer:
            raise HTTPException(
                status_code=500, detail=f"{Customer} could not be found"
            )
        return CustomerResponseModel.model_validate(customer, from_attributes=True)


@router.post(
    path="/order",
    summary="Create order",
    tags=["Order"],
    response_model=OrderResponseModel,
)
async def create_order(
    customer_id: int = Query(..., title="Customer IDs"),
    products_ids: List[int] = Body(..., title="Product IDs"),
):
    """Create order"""
    async with uow:
        uow.register_repository(Customer, BaseRepository)
        uow.register_repository(Product, BaseRepository)
        uow.register_repository(Order, BaseRepository)
        order = await warehouse_service.create_order(customer_id, products_ids)
        if not order:
            raise HTTPException(status_code=500, detail=f"{Order} could not be created")
        return OrderResponseModel.model_validate(order, from_attributes=True)


@router.get(
    path="/order",
    summary="Get order by ID",
    tags=["Order"],
    response_model=OrderResponseModel,
)
async def get_order(order_id: int = Query(..., title="Order ID")):
    """Get order by ID"""
    async with uow:
        uow.register_repository(Order, BaseRepository)
        order = await uow.get_repository(Order).get(obj_id=order_id)
        if not order:
            raise HTTPException(status_code=500, detail=f"{Order} could not be found")
        return OrderResponseModel.model_validate(order, from_attributes=True)


@router.post(
    path="/product",
    summary="Add product",
    tags=["Product"],
    response_model=ProductResponseModel,
)
async def add_product(
    name: str = Body(..., title="Name"),
    quantity: int = Body(..., title="Quantity"),
    price: float = Body(..., title="Price"),
):
    """Add product"""
    customer = CustomerDTO(
        id=1,
        orders=[
            OrderDTO(
                id=1, products=[ProductDTO(id=1, name="banana", quantity=1, price=100)]
            )
        ],
    )
    logger.info(customer.as_dict())
    async with uow:
        uow.register_repository(Product, BaseRepository)
        product = await warehouse_service.create_product(
            ProductDTO(name=name, quantity=quantity, price=price)
        )
        if not product:
            raise HTTPException(status_code=500, detail=f"{Product} could not be added")
        return ProductResponseModel.model_validate(product)


@router.get(
    path="/product",
    summary="Get product by ID",
    tags=["Product"],
    response_model=ProductResponseModel,
)
async def get_product(
    product_id: int = Query(..., title="product_id"),
):
    """Get product by ID"""
    async with uow:
        uow.register_repository(Product, BaseRepository)
        product = await warehouse_service.get_product(product_id)
        if not product:
            raise HTTPException(
                status_code=500, detail=f"{Product} could not be founded"
            )
        return ProductResponseModel.model_validate(product)
