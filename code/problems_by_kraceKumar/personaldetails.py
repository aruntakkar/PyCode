"""
Write a program to display your details like name, age, address.
"""


def main():
    name = "arun"
    age = 24
    address = "Arun Rohtak Haryana"

    # we can also use the ("%s %s %s" % (name , age, address)) Approach

    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

    # To give placeholder an explicit positonal index
    # This allow for re-arranging the order of display
    # print("{1} {0} {2}" .format(age, name, address))

# __name__ holds the name of the current modulce
if __name__ == "__main__":
    main()
