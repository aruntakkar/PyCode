class Animal(object):

    def __init__(self, name):
        self.name = name

zebra = Animal("Jeffrey")
print(zebra.name)

# we can access attributes of our objects using
# dot notation


class Square(object):

    def __init__(self):
        self.sides = 4

my_shape = Square()
print(my_shape.sides)

"""
firstly we create a class Square with an attribute sides,
Outside the class definition, we create a new instance
of Square named my_shape and access that attribute usin
my_shape.sides
"""
