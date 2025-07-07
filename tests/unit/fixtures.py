import pytest

from domain.dtos import CustomerDTO, OrderDTO, ProductDTO

dto_fixtures = [
    pytest.param(
        ProductDTO(id=1, name="Banana", quantity=1, price=100),
        {"id": 1, "name": "Banana", "quantity": 1, "price": 100},
        id="DTO TO DICT: Product",
    ),
    pytest.param(
        OrderDTO(
            id=1,
            products=[
                ProductDTO(id=1, name="Banana", quantity=1, price=100),
                ProductDTO(id=2, name="Apple", quantity=1, price=200),
                ProductDTO(id=3, name="Peach", quantity=1, price=400),
            ],
        ),
        {
            "id": 1,
            "products": [
                {"id": 1, "name": "Banana", "quantity": 1, "price": 100},
                {"id": 2, "name": "Apple", "quantity": 1, "price": 200},
                {"id": 3, "name": "Peach", "quantity": 1, "price": 400},
            ],
        },
        id="DTO TO DICT: Order",
    ),
    pytest.param(
        CustomerDTO(
            id=1,
            orders=[
                OrderDTO(
                    id=1,
                    products=[
                        ProductDTO(id=1, name="Banana", quantity=1, price=100),
                        ProductDTO(id=2, name="Apple", quantity=1, price=200),
                        ProductDTO(id=3, name="Peach", quantity=1, price=400),
                    ],
                ),
                OrderDTO(
                    id=2,
                    products=[
                        ProductDTO(id=4, name="Potato", quantity=1, price=100),
                        ProductDTO(id=5, name="Cucumber", quantity=1, price=200),
                        ProductDTO(id=6, name="Tomato", quantity=1, price=400),
                    ],
                ),
            ],
        ),
        {
            "id": 1,
            "orders": [
                {
                    "id": 1,
                    "products": [
                        {"id": 1, "name": "Banana", "quantity": 1, "price": 100},
                        {"id": 2, "name": "Apple", "quantity": 1, "price": 200},
                        {"id": 3, "name": "Peach", "quantity": 1, "price": 400},
                    ],
                },
                {
                    "id": 2,
                    "products": [
                        {"id": 4, "name": "Potato", "quantity": 1, "price": 100},
                        {"id": 5, "name": "Cucumber", "quantity": 1, "price": 200},
                        {"id": 6, "name": "Tomato", "quantity": 1, "price": 400},
                    ],
                },
            ],
        },
        id="DTO TO DICT: Customer",
    ),
]
