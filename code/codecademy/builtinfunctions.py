def biggest_number(*args):
    print(max(args))
    return max(args)


def smallest_number(*args):
    print(min(args))
    return min(args)


# abs() function returns the absolute value of number it takes as an argument
# that is the number distance from 0 on an imagined number line.
def distance_from_zero(arg):
    print(abs(arg))
    return abs(arg)

# type() function returns the type of data it recives as argument
print(type(4))
print(type(4.5))
print(type('spam'))

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)
