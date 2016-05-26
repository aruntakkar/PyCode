import heapq

grades = [30, 20, 40, 50, 10]

largest_grades = heapq.nlargest(2, grades)
print(largest_grades)

stocks = [
    {'Stock': 'GOOG', 'Price': 201},
    {'Stock': 'AAPL', 'Price': 800},
    {'Stock': 'F', 'Price': 54},
    {'Stock': 'AMZN', 'Price': 313},
    {'Stock': 'F', 'Price': 313},
    {'Stock': 'MSFT', 'Price': 68}
]

print(heapq.nsmallest(2, stocks, key=lambda stocks: stocks['Price']))
