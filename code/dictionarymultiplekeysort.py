from operator import itemgetter

stocks = [
    {'Stock': 'GOOG', 'Price': 201},
    {'Stock': 'AAPL', 'Price': 800},
    {'Stock': 'F', 'Price': 54},
    {'Stock': 'AMZN', 'Price': 313},
    {'Stock': 'F', 'Price': 313},
    {'Stock': 'MSFT', 'Price': 68},
    {'Stock': 'MSFT', 'Price': 98},
    {'Stock': 'MSFT', 'Price': 23},
]

for x in sorted(stocks, key=itemgetter('Stock')):
    print(x)

print("---")

# Again Sorting for Duplicate items by After first sort of Stock By Price
for x in sorted(stocks, key=itemgetter('Stock', 'Price')):
    print(x)
