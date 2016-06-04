"""
    It is used when a statement is required syntactically
    , but you don't want any command or code to execute.
    pass statement is a null operation, nothing happens when it executes.
"""

# Example

for letter in "Python":
    if letter == "h":
        pass
        print("This is pass block")
    print("Current letter :", letter)

print("Good Bye")
