stocks = {
    'GOOG': 434,
    'AAPL': 325,
    'FB': 54,
    'AMZN': 623,
    'F': 32,
    'MSFT': 549
}

# Performing the calculation based on dictionary values
# Zip combines the list and return as set of touples

min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)
