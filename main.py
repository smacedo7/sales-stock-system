
from models.customer import Customer
from models.inventory import Inventory
from models.product import Product
from models.shopping_cart import ShoppingCart
from services.checkout import CheckoutService


def main():

    product1 = Product(
        name='Martelo',
        description='Ferramenta para construção',
        price=27.99
    )

    inventory1 = Inventory()
    inventory1.add_product(
        product=product1,
        initial_quantity=0
    )
    inventory1.increase_stock(
        product=product1,
        quantity=10
    )

    customer1 = Customer(
        name="Samuel Macedo Correia",
        cpf="12345678912",
        address="Wall Street, Baxter building",
        email="richlittledev@gmail.com",
        balance=500
    )

    cart1 = ShoppingCart(customer=customer1)
    cart1.add_product(product=product1)

    print("Stock before:", inventory1.get_quantity(product=product1))
    print("Balance before:", customer1.balance)
    print("Cart total:", cart1.total)

    sale = CheckoutService.checkout(
        cart=cart1,
        inventory=inventory1
    )

    print("Sale total:", sale.total)
    print("Balance after:", customer1.balance)
    print("Stock after:", inventory1.get_quantity(product=product1))
    print("Cart after:", cart1.items)

    product1 = Product(
        name="Martelo",
        price=27.99,
        description="Ferramenta para construção",
    )

    data = product1.to_dict()

    product2 = Product.from_dict(data)

    print(data)
    print(product2.id)
    print(product2.name)
    print(product2.price)
    print(product2.description)


if __name__ == "__main__":
    main()
