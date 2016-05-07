"""
 - Cost of meal = $44.50
 - Restaurant tax = 6.75%
 - Tip = 15%

 You'll apply the tip to the overall cost of the meal (inculding tax)
"""
meal = 44.50

tax = 6.75 / 100

tip = 15 / 100

meal = meal + meal * tax

total = meal + meal * tip

# code on this line prints to console the value of total with 2 decimal
print("%.2f" % total)
