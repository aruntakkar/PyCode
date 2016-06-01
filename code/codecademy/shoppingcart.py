class ShoppingCart():
    items_in_cart = {}

    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        if product not in self.items_in_cart:
            self.items_in_cart[product] = price
            print(product + " added")
        else:
            print(product + " already in the stock")

    def remove_item(self, product):
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print(product + " removed")
        else:
            print(product + " is not in the cart")

my_cart = ShoppingCart("Eric")
my_cart.add_item("Butter", 500)
