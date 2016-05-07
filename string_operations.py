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
