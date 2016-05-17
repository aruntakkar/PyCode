# Passing the Default Value for the arguments
def dumb_sentence(name="Arun", action="ate", item="fish"):
    print(name, action, item)

# calling the function with default arguments
dumb_sentence()

"""
caling the function with the values for argmument
first one is for the name and so on according to arguments
"""
dumb_sentence("Deepak", "wash", "car")

# Sending the arguments without worry about order of arguments
dumb_sentence(item="Burger")

# Calling the function with the two arguments
dumb_sentence(item="awesome", action="is")
