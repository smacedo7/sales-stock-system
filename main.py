from models.product import Product
from models.inventory_item import InventoryItem
from models.inventory import Inventory

def main():

    cibola = Product('maca', 'fruta vermleha', 2.99)
    cibolitos = InventoryItem(cibola, 5)
    print(cibolitos.quantity)
    cibolitos.increase(10)
    print(cibolitos.quantity)
    cibolitos.decrease(7)
    print(cibolitos.quantity)
    birosca = Inventory()
    birosca.increase_stock()

if __name__ == "__main__":
    main()
