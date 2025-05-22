"""Здесь мы храним схемы таблицы. Ок"""

from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    quantity = Column(Integer)
    price = Column(Float)


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, autoincrement=True)


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, autoincrement=True)


order_product_assocoations = Table(
    "order_product_assocoations",
    Base.metadata,
    Column("order_id", ForeignKey("orders.id")),
    Column("product_id", ForeignKey("products.id")),
)

customer_order_assocoations = Table(
    "customer_order_assocoations",
    Base.metadata,
    Column("customer_id", ForeignKey("customers.id")),
    Column("order_id", ForeignKey("orders.id")),
)

Order.products = relationship(
    "Product", secondary=order_product_assocoations, lazy="selectin"
)
Customer.orders = relationship(
    "Order", secondary=customer_order_assocoations, lazy="selectin"
)
