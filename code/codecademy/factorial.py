def factorial(x):
    product = 1
    for i in range(x):
        product = product * (i + 1)
    return product

print(factorial(4))
