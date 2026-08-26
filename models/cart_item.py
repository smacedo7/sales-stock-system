from models.product import Product


class CartItem:
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
            raise ValueError('Quantity must be greater than zero. ')

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

        self._quantity -= quantity

    @property
    def subtotal(self) -> float:
        return self._product.price * self._quantity

    @property
    def product(self) -> Product:
        return self._product

    @property
    def quantity(self) -> int:
        return self._quantity
