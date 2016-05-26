def digit_sum(number):
    string = str(number)
    total = 0
    for c in string:
        total += int(c)
    print("The Sum of number is:", total)
    return total

digit_sum(434)
