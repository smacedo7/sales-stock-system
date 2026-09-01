from models.customer import Customer
from models.inventory import Inventory
from models.sale import Sale
from models.sale_item import SaleItem
from models.shopping_cart import ShoppingCart


class CheckoutService:
    @staticmethod
    def checkout(
            cart: ShoppingCart,
            inventory: Inventory
    ) -> Sale:

        CheckoutService._validate_cart(cart)
        CheckoutService._validate_stock(cart=cart, inventory=inventory)

        customer = cart.customer
        CheckoutService._validate_balance(customer=customer, cart=cart)
        
        sale_items = CheckoutService._create_sale_items(cart=cart)
        sale =  Sale(customer=customer, items=sale_items)

        customer.charge(cart.total)
        

        for item in cart.items.values():
            inventory.decrease_stock(
                product=item.product,
                quantity=item.quantity
            )


        cart.clear()

        return sale

    @staticmethod
    def _validate_cart(cart: ShoppingCart) -> None:
        if not isinstance(cart, ShoppingCart):
            raise TypeError('Cart must be a ShoppingCart instance.')
        if not cart.items:
            raise ValueError('Cart cannot be empty.')

    @staticmethod
    def _validate_stock(cart: ShoppingCart, inventory: Inventory) -> None:
        if not isinstance(inventory, Inventory):
            raise TypeError('Inventory must be an Inventory instance.')
        for item in cart.items.values():
            available_quantity = inventory.get_quantity(item.product)

            if available_quantity < item.quantity:
                raise ValueError(
                    f'Insufficient stock for product "{item.product.name}".'
                )     

    @staticmethod
    def _validate_balance(customer: Customer, cart: ShoppingCart) -> None:
        if not isinstance(customer, Customer):
            raise TypeError('Customer must be a Customer instance.')
        if customer.balance < cart.total:
            raise ValueError('Insufficient balance.')

    @staticmethod
    def _create_sale_items(cart: ShoppingCart) -> list[SaleItem]:
        sale_items = []
        for item in cart.items.values():
            sale_item = SaleItem(
                product=item.product,
                quantity=item.quantity
            )
            sale_items.append(sale_item)
        return sale_items

