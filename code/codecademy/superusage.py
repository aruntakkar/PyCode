"""
    Sometimes we need the method that we override in child class, but we need
    themfrom the parent class then we can use the super builtin.
"""
class Employee(object):

    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00


class PartTimeEmployee(Employee):

    def calcualate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):
        self.hours = hours
        # Syntax in python 2 > super(parent_class, self).method(args)
        # Syntax in python 3 > super().method(args)
        return super().calculate_wage(hours)

milton = PartTimeEmployee("Guido")
print(milton.full_time_wage(12))
