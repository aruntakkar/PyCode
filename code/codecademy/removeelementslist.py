"""
    n.pop(index) will remove the item from the item at index from the list
    and return it you.
"""
# n.pop(index)

"""
    n.remove(item) will remove the actual item if it finds it
"""
# n.remove(item)

"""
    del(n[1]) is like n.pop(index) will remove the item at given index but
    did'nt return anything.
"""
# del(n[1])

n = [1, 3, 5]

n.pop(1)
# Returns 3(the item at index at 1)
print(n)

# remove the 1 from the list not the element at index 1
n.remove(1)

print(n)

# del(n[1]) is like .pop remove the particular index element
#  But it did'nt return Anything
del(n[0])

print(n)
