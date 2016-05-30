# simple example of list comprehension
new_list = [x for x in range(1, 6)]
# gives [1,2,3,4,5]

# if you want number doubles
doubles = [x * 2 for x in range(1, 6)]
# gives [2,4,6,8,10]

# if you want double number divisble by three
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# even number between 1 to 50
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print(evens_to_50)

# even number squarred b/w 1 to 10
even_squares = [x**2 for x in range(1, 11) if x**2 % 2 == 0]
print(even_squares)

# this list prints ['C', 'C', 'C']
c = ['C' for x in range(5) if x < 3]
print(c)

# cubes of number divisble by 4
cubes_by_four = [x**3 for x in range(1, 11) if (x**3) % 4 == 0]
print(cubes_by_four)

# if you don't pass the particular index to the list slice, python will pick
# a default

to_five = ['A', 'B', 'C', 'D', 'E']

print(to_five[3:])
# Prints ['D', 'E']

print(to_five[:2])
# Prints ['A', 'B']

print(to_five[::2])
# Prints ['A', 'C' 'E']

my_list = range(1, 11)  # List of numbers 1 - 10

# odd numbers
print(my_list[::2])

# A negative stride progress through the list from right to left
backwards = ['E', 'D', 'C', 'B', 'A']
print(backwards[::-1])


my_list = range(1, 11)

# A negative stride progress through the list from right to left
backwards = my_list[::-1]
print(backwards)


to_one_hundred = range(101)
# Add your code below!

backwards_by_tens = to_one_hundred[0:110:10]
print(backwards_by_tens)

to_21 = range(1, 22)
odds = to_21[0:22:2]
middle_third = to_21[7:14:1]
print(middle_third)
