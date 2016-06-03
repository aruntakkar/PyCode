"""
    Write a program to print fizz, buzz or fizzbuzz if
    one of the conditions is meet.

    If the number is a multiple of 3, print fizz
    a multiple of 5, print buzz

    and if a multiple of both 3 and 5, print fizzbuzz.
"""

# Here we are using pass statement
# when a statement is required syntactically, but you don't want any
# command or code to execute.


def main():
    num = 15
    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif (num % 3 == 0) and (num % 5 == 0):
        print("FizzBuzz")
    else:
        print("Cool No Buzz Word")

# __name__ holds the name of the current module
if __name__ == "__main__":
    main()
