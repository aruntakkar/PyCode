income = [10, 30, 75]


def double_income(dollars):
    return dollars * 2

"""
    By Map:- Take a list you can Run each item of list
    through a function.
"""

new_income = list(map(double_income, income))
print(new_income)
