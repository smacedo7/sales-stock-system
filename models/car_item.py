from models.product import Product


class CarItem:
    def __init__(
            self,
            product: Product,
            quantity: int = 1,
    ) -> None:
        self._validate_product(product)
        self._validate_quantity(quantity)

        self._product = product
        self._quantity = quantity

    def _validate_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError('Product must be a Product instance. ')

    def _validate_quantity(self, quantity: int) -> None:
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError('Quantity must be an integer.')

        if quantity < 0:
            raise ValueError('Quantity must be greater than or equal to zero. ')

    def increase(self, quantity) -> None:
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError('Quantity must be an integer. ')
        if quantity <= 0:
            raise ValueError('Quantity must be greater than zero.')

        self._quantity += quantity

    def decrease(self, quantity: int) -> None:
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError('Quantity must be an integer.')
        if quantity <= 0:
            raise ValueError('Quantity must be greater than zero.')
        if self._quantity < quantity:
            raise ValueError('Insufficient stock.')

    @property
    def subtotal(self) -> float:
        return self._product * self._quantity
