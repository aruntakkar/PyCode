"""
    A  Parameter acts as a variable named for a passed in arguments
    A Function can require as many parameters as you like, but when you
    call the function matching number of arguments must be passed.
"""


def power(base, exponent):  # Add your parameters here
    result = base**exponent
    print("%d to the power of %d is %d" % (base, exponent, result))

power(37, 4)  # Add your arguments Here
