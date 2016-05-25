"""
    In this example loop will break if 5 is generated,
    the else will not be executed, otherwise after 3
    numbers are generated, the loop condition will become
    false and the else will be executed.
"""

from random import randint

print("Lucky Numbers! 3 numbers will be generated.")
print("If one of them is a '5', you lose!")

count = 0
while count < 3:
    num = randint(1, 6)
    print(num)
    if num == 5:
        print("sorry you lose")
        break
    count += 1
else:
    print("You won!")
