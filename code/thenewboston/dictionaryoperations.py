# min and max and sorting dictionary

stocks = {
    'Google': 520.24,
    'FB': 76.95,
    'Yahoo': 39.28,
    'Amazon': 306.71,
    'Apple': 99.76
}

# you can not sort the dictionary but you can able to sort the list

print(min(zip(stocks.values(), stocks.keys())))

print(max(zip(stocks.values(), stocks.keys())))

print(sorted(zip(stocks.values(), stocks.keys())))
