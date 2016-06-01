"""
    Inheritence is the process by which one class takes on the attributes
    and methods of another, and it is used to express an (is-a) relationship.
"""


class Customer(object):
    """ Produces object that represents customers."""

    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(cart):
        print("I am a string that stands in for the contents of your shopping cart!")


class ReturningCustomers(Customer):
    """ For the customer of the Repeat Variety."""

    def display_order_history(self):
        print("I am a string that stands in for your order history!")

monty_python = ReturningCustomers("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()
