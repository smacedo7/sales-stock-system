from models.product import Product
from models.inventory_item import InventoryItem
from models.inventory import Inventory
from models.customer import Customer

import re



def main():

    cliente1 = Customer(
        'Samuel Macedo',
        '05852806145',
        'Rua das Figueiras, Cond. Ilha de Patmos, Cs 01',
        'samucamaiscedo@gmail.com',
        50
    )

    print(cliente1.id)
    print(cliente1.name)
    print(cliente1.balance)
    print(cliente1.address)
    print(cliente1.cpf)
    print(cliente1.email)
    cliente1.deposit(100)
    print(cliente1.balance)
    cliente1.charge(77)
    print(cliente1.balance)


if __name__ == "__main__":
    main()
