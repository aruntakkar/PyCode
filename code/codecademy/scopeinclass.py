class Animals(object):
    is_alive = True

    def __init__(self, name, age):
        self.name = name
        self.age = age
"""
    Note that each individual animal gets its name, age
    Since they are all intialized individually,
    but they have access to the member variable is_alive
"""

zebra = Animals("Jeffery", 2)
Tiger = Animals("Robin", 4)
Panda = Animals("Dodo", 5)

print(zebra.name, zebra.age, zebra.is_alive)
print(Tiger.name, Tiger.age, Tiger.is_alive)
print(Panda.name, Panda.age, Panda.is_alive)
