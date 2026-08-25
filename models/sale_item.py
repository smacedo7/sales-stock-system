from models.product import Product


class SaleItem:
    
    """
    Represents a snapshot of a product sold during a sale.

    Stores immutable product information so that future
    product updates do not affect historical sales.
    """

    def __init__(
            self,
            product: Product,
            quantity: int
    ) -> None:
        self._validate_product(product)
        self._validate_quantity(quantity)

        self._product_id = product.id
        self._product_name = product.name
        self._unit_price = product.price
        self._quantity = quantity

    def _validate_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError('Product must be a Product instance. ')

    def _validate_quantity(self, quantity: int) -> None:
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError('Quantity must be an integer.')
        if quantity <= 0:
            raise ValueError('Quantity must be greater than zero')

    @property
    def product_id(self) -> int:
        return self._product_id

    @property
    def product_name(self) -> str:
        return self._product_name

    @property
    def unit_price(self) -> float:
        return self._unit_price

    @property
    def quantity(self) -> int:
        return self._quantity

    @property
    def subtotal(self) -> float:
        return self._unit_price * self._quantity
