class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print self.name
        print self.age

hippo = Animal("Zanda", 5)
sloth = Animal("Bucky", 10)
ocelot = Animal("Rave", 20)

# change the value of is_alive for hippo
hippo.is_alive = False
print hippo.is_alive

print hippo.health
print sloth.health
print ocelot.health
