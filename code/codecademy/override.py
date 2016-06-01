"""
    Sometimes we want one class that inherits from the another
    to not only take on the methods and attributes of its parent
    but, to override one or more of them
"""


class Employee(object):

    def __init__(self, name):
        self.name = name

    def greet(self, other):
        print("Hello %s" % other.name)


class CEO(Employee):

    def greet(self, other):
        print("Get back to work %s" % other.name)

ceo = CEO("Emily")
emp = Employee("Steve")

emp.greet(ceo)
# Hello, Emily

ceo.greet(emp)
# Get back to work, Steve


"""
    Rather than have a separate greet_underling method for
    our CEO, We override(or-re-create) the greet method on top
    of the Base (Employee.greet) method.(This way, we don't need
    to know what type of Employee we have, before We Greet another Employee.)
"""
