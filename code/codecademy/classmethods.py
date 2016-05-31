class Animal(object):
    is_alive = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    """
        When a class has its own functions, those functions are called methods

        a new method description it print out the name and age of animal it's

        called on.

        Remember to pass self as an argument to description  otherwise,

        printing self.name and self.age won't work

        since Python won't know which self(that is, which object),

        you're talking about!
    """

    def description(self):
        print self.name
        print self.age

hippo = Animal("Zanda", 5)
hippo.description()
