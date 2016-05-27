def is_prime(x):
    if x > 1:
        # the smallest prime is 2, we start the divisor at 3
        divisor = 2

        # because the submit number can always be divided by itself we can use
        # this range function to set the correct range
        for i in range(divisor, x):
            if (x % i) == 0:
                print("Not a Prime Number")
                return False

    else:
        print("Prime can only be a Positive Number")
        return False

    print("Prime Number")
    return True

is_prime(-4)
is_prime(4)
is_prime(5)
