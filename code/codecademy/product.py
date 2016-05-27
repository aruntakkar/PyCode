def product(products):
    total = 1
    for item in products:
        total *= item
    print(total)
    return total

product([4, 5, 5])
