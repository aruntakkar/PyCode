# once = {
#     'a': 1,
#     'b': 2
# }

# twice = {
#     'a': 2,
#     'b': 4
# }

# for key in once:
#     print("Once: %s" % once[key])
#     print("Twice: %s" % twice[key])

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}

stocks = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
total = 0

for key in prices:
    print(key)
    print("Price: %s" % prices[key])
    print("Stock: %s" % stocks[key])
    # total Value
    value = prices[key] + stocks[key]
    total = total + value
print("total income %s" % total)
