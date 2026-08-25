from datetime import datetime

from models.customer import Customer
from models.sale_item import SaleItem


class Sale:
    _next_id = 1

    def __init__(
            self,
            customer: Customer,
            items: list[SaleItem]
    ) -> None:
        self._validate_customer(customer)
        self._validate_items(items)

        self._items = items.copy()
        self._customer_name = customer.name
        self._customer_id = customer.id
        self._created_at = datetime.now()  # noqa: DTZ005
        
        self._id = type(self)._next_id
        type(self)._next_id += 1

    def _validate_customer(
            self,
            customer: Customer
    ) -> None:
        if not isinstance(customer, Customer):
            raise TypeError('Customer must be a Customer instance.')

    def _validate_items(
            self,
            items: list[SaleItem],
    ) -> None:
        if not isinstance(items, list):
            raise TypeError('Items must be a list.')
        if not items:
            raise ValueError('Items cannot be empty.')
        for item in items:
            if not isinstance(item, SaleItem):
                raise TypeError('Item must be a SaleItem object.')

    @property
    def customer_id(self) -> int:
        return self._customer_id

    @property
    def customer_name(self) -> str:
        return self._customer_name

    @property
    def id(self) -> int:
        return self._id

    @property
    def items(self) -> list[SaleItem]:
        return self._items.copy()

    @property
    def total(self) -> float:
        return sum(item.subtotal for item in self._items)

    @property
    def created_at(self) -> datetime:
        return self._created_at
