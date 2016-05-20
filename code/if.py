age = int(input("Tell your Age?"))

if age < 21:
    print("no beer for you")
elif age > 21:
    print("beer for you")

"""
    if any condition elif not pass than else will be run
    Non of elif is pass (if you run through all the option nothing is true
    than run else)
"""

name = "Lucy"

if name is "Bucky":
    print("Hey there Bucky")
elif name is "Lucy":
    print("What up LucDog?")
elif name is "Sammy":
    print("Hey Slammi")
else:
    print("please sign up %s" % (name))


name = eval(input("Enter your name?"))

if name is "arun":
    print("Hey arun")
elif name is "sunny":
    print("Hey sunny")
else:
    print("no name is Entered")
