"""
    enumerate works by supplying a corresponding index
    to each element, in the list that you pass it
"""

"""
    Each time you go through loop, index will be one greater,
    & item will be Next item in the Sequence.
"""

choices = ['pizza', 'pasta', 'salad', 'nachos']

print('Your choices are:')
for index, item in enumerate(choices):
    print(index + 1, item)
