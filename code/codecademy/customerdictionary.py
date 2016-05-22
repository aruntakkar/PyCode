# Now customer need to know how much is spending on groceries list
# if product in stock than only add item price in total

# using for loops with lists and dictionaries

# writing functions with loops, lists, and dictonaries

# Updating data in respone to changes in the enviorment

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
    return total

compute_bill(shopping_list)
