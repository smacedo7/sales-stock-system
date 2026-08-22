from models.cart_item import CartItem
from models.customer import Customer
from models.product import Product


class ShoppingCart:
    def __init__(
            self,
            customer: Customer
    ) -> None:

        self._validate_customer(customer)
        self._customer = customer
        self._items = {}

    def _get_item(self, product: Product) -> CartItem:

        self._validate_product(product)

        if product.id not in self._items:
            raise KeyError('Product not found in cart.')
        
        return self._items[product.id]
    
    def _validate_customer(
            self,
            customer: Customer
    ) -> None:
        if not isinstance(customer, Customer):
            raise TypeError('Customer must be a Customer instance.')
        
    def _validate_product(
            self,
            product: Product
    ) -> None:
        if not isinstance(product, Product):
            raise TypeError('Product must be a Product instance. ')

    def add_product(
            self,
            product: Product
    ) -> None:
        self._validate_product(product)

        if product.id in self._items:
            self.increase_quantity(product)
        else:
            self._items[product.id] = CartItem(product)

    def remove_product(
            self,
            product: Product
    ) -> None:
        self._validate_product(product)

        if product.id in self._items:
            del self._items[product.id]
        else:
            raise KeyError('Product not found in cart.')

    def increase_quantity(
            self,
            product: Product,
            quantity: int = 1
    ) -> None:
        item = self._get_item(product)
        item.increase(quantity)

    def decrease_quantity(
            self,
            product: Product,
            quantity: int = 1
    ) -> None:
        item = self._get_item(product)
        item.decrease(quantity)
        if item.quantity == 0:
            del self._items[product.id]

    def clear(self) -> None:
        self._items.clear()

    @property
    def total(self) -> float:
        return sum(number.subtotal for number in self._items.values())

    @property
    def items(self):
        return self._items.copy()