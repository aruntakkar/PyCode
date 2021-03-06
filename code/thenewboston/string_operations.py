# print simply display your code in console

# print a string
print("Welcome to Python 101")

# print a variable
my_machine_goes = "Ping!"

print(my_machine_goes)

# printing the strings with concatenation
print("I " + "love " + "Python")

"""
 Sometimes you need to combine a string with something that isn't string.
 In order to do that, you have to convert the non-string into a string.
"""
# Here str converts non strings to strings
print("I have " + str(2) + " coconuts!")

"""
 When you want to print string with other strings there is a better method than
 concatenation string together is %
 the % operator after a string is used to combine a string with variables.
 the % operator will replace a %s in the string with the string variable that
 comes after it.
"""

string_1 = "noida,"
string_2 = "gurugram from gurgaon."

# combine string with variables
print("lets go to %s Silly move of Govt %s" % (string_1, string_2))

"""
 you need same number of %s terms in a string as the numbers of
 variables/strings in parentheses:
"""
name = "arun"
color = "grey"
dream = "Great Programmer"

print("The %s favourite color is %s dream to become %s" % (name, color, dream))

# same about example with the input for variables

name = input("What is your name?")
color = input("What is your favourite color")
dream = input("dream to Become?")

print("Ah your name is %s , color: %s, dream: %s" % (name, color, dream))

"""
 Three ways to create the strings
"""
'Alpha'
"Bravo"
str(3)

"""
 string methods
"""
len("charlie")
"Delta".upper()
"Echo".lower()

# printing a string
print("Foxtrot")

# Advance Printing techniques
g = "Golf"
h = "Hotel"

print("%s , %s" % (g, h))

# To print in the New line in the new line use \n
print("ok\nnumbers")

# To Print Raw String like file path so it don't have special meaning
print(r"c\users\hp\nnumbers")

"""
slicing a string with number of charactrers in the string
"""

string = "Test String"

# print first character of string
print(string[0])

# print last character of string
print(string[-1])

# print the character b/w 2-4 it gives the string characters 2,3 not the 4
print(string[2:4])
