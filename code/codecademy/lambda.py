"""
    In Python you are allowded to pass functions around just as if
    they were variables or values. (anonymous functions)
"""

my_list = range(16)
# when we pass the lambda to filter uses the
# lambda to determine what to filter
# the second argument it does the filtering on.
print(filter(lambda x: x % 3 == 0, my_list))

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print(filter(lambda x: x == "Python", languages))

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXX \
    XXgXeX!XX"

message = filter(lambda x: x != "X", garbled)

print(message)
