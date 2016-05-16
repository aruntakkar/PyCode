"""
The statement return[expression] exists a function, optionally passing back an
expression to the caller. A return statement with no arguments is the same as
retrun None
"""


# Function to Get the Girlfriend age limit according to when you calling
def allowded_dating_age(my_age):
    girls_age = my_age/2 + 7
    # What you want back from this function return the value
    return girls_age

arun_limit = allowded_dating_age(24)
sunny_limit = allowded_dating_age(28)

print("arun can date girls", arun_limit, "or older")
print("sunny can date girls", sunny_limit, "or older")


# Function to Get the dude age and girl age b/w 15-60
def age_table(age):
    girls_age = age/2 + 7
    return girls_age

print('dude_age', 'girl_age')
for x in range(15, 61):
    girlfriend_age = age_table(x)
    print(x, '\t', girlfriend_age)
