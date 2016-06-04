first_name = ['arun', 'sunny', 'robert']
last_name = ['takkar', 'dev', 'goe']

name = zip(first_name, last_name)

# By zip function we get list of tuples according to number of elements
# [('arun', 'takkar'), ('sunny', 'nasa'), ('robert', 'goe')]

for a, b in name:
    print(a, b)
