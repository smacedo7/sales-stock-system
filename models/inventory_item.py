from models.product import Product

class InventoryItem:
    def __init__(self, product, quantity):
        self._validate_product(product)
        self._validate_quantity(quantity)

        self._product = product
        self._quantity = quantity

    @property
    def quantity(self):
        return self._quantity
    
    @property
    def product(self):
        return self._product

    def _validate_product(self, product):
        if not isinstance(product, Product):
            raise TypeError('Product must be a Product instance. ')
    
    def _validate_quantity(self, quantity):
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError('Quantity must be an integer.')
        
        if quantity < 0:
            raise ValueError('Quantity must be greater than or equal to zero. ')

    def increase(self, quantity):
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError('Quantity must be an integer. ')
        if quantity <= 0:
            raise ValueError('Quantity must be greater than zero.')

        self._quantity += quantity

    def decrease(self, quantity):
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError('Quantity must be an integer.')
        if quantity <= 0:
            raise ValueError('Quantity must be greater than zero.')
        if self._quantity < quantity:
            raise ValueError('Insufficient stock.')

        self._quantity -= quantity

    def __repr__(self):
        return f'Product: {self._product}, Quantity: {self._quantity}'
