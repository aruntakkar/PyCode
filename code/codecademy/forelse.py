"""
    In this case, the else statement is executed after
    the for loop, but only if the for ends normally,
    that is not with the break after matching the tomato
    condition.

"""

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print("You have...")
for f in fruits:
    if f == 'tomato':
        print("A tomato is a fruit!")
    print("A", f)
else:
    print("A Fine Collection of Fruits!")

# Another implementation of for else

names = {'arun': '5/1/1992', 'sunny': '1/5/1998',
         'monty': '1/9/1999', 'dev': '6/3/1998'}

for key in names:
    print key, names[key]
    if key == 'arun':
        print "arun is in the dictionary"
else:
    print "You get all the value in the dictionary"
