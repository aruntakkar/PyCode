import heapq

grades = [30, 20, 40, 50, 10]

largest_grades = heapq.nlargest(2, grades)
print(largest_grades)

stocks = [
    {'Ticker': 'GOOG', 'Price': 201},
    {'Ticker': 'AAPL', 'Price': 800},
    {'Ticker': 'F', 'Price': 54},
    {'Ticker': 'AMZN', 'Price': 313},
    {'Ticker': 'F', 'Price': 313},
    {'Ticker': 'MSFT', 'Price': 68}
]

print(heapq.nsmallest(2, stocks, key=lambda stock: stock['Price']))
