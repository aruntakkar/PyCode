class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        return "This is a %s %s with %s MPG. " % (self.color, self.model, self.mpg)

    def drive_car(self):
        self.condition = "used"

my_car = Car("DeLorean", "silver", 88)

print(my_car.condition)
print(my_car.drive_car())
print(my_car.condition)


class ElectricCar(Car):

    def __init__(self, model, color, mpg, battery_type):
        super().__init__(model, color, mpg)
        self.battery_type = battery_type

    def display_car(self):
        inherit_str = super().display_car()
        return inherit_str + "It has a %s battery. " % (self.battery_type)

my_electric_car = ElectricCar("Ford", "white", 88, "molten salt")

print(my_electric_car.display_car())
