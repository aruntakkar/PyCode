def cube(number):
    number = number**3


def by_three(number):
    if number % 3 == 0:
        number = cube(number)
        return number
    else:
        return False
by_three(6)
