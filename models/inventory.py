from models.product import Product
from models.inventory_item import InventoryItem

class Inventory:
    def __init__(self):
        self._items = {}
    
    def _validate_product(self, product):
        if not isinstance(product, Product):
            raise TypeError('Product must be a Product instance ')

    def _get_item(self, product):
        self._validate_product(product)
        if product.id not in self._items:
            raise ValueError('Product not found')
        return self._items[product.id]

    def add_product(self, product, initial_quantity=0):
        self._validate_product(product)
        if product.id in self._items:
            raise ValueError('Product is already registered. ')
        self._items[product.id] = InventoryItem(product, initial_quantity)
    
    def increase_stock(self, product, quantity):
        item = self._get_item(product)
        item.increase(quantity)
    
    def decrease_stock(self, product, quantity):
        item = self._get_item(product)
        item.decrease(quantity)
