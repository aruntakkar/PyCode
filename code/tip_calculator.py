# """
#  - Cost of meal = $44.50
#  - Restaurant tax = 6.75%
#  - Tip = 15%

#  You'll apply the tip to the overall cost of the meal (inculding tax)
# """
# meal = 44.50

# tax = 6.75 / 100

# tip = 15 / 100

# meal = meal + meal * tax

# total = meal + meal * tip

# # code on this line prints to console the value of total with 2 decimal
# print("%.2f" % total)


""" Calculator with Functions """


def tax(bill):
    """ Adds 8% tax to a restaurant bill """
    bill *= 1.08
    print("with tax: %f" % bill)
    return bill


def tip(bill):
    """ Adds 15% tip to restaurant bill """
    bill *= 1.15
    print("with tip: %f" % bill)
    return bill

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tax(meal_with_tax)
