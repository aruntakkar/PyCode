"""
Sets is used for Collection of itemes Where duplication is useless
Unordered collection of Unique elements
"""

groceries = {'jam', 'butter', 'fish', 'beer', 'tape', 'pickle', 'beer', 'milk'}

# when using groceries set it don't give the duplicate data
print(groceries)

if 'milk' in groceries:
    print("You already have milk boss!")
else:
    print("oh Yes, you need milk!")
