inventory = {
    'gold': 500,
    # Assigned a new list to 'pouch' key
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here

# Adding a 'pocket' key to inventory
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# sorting the list found under the key 'backpack'
inventory['backpack'].sort()

inventory['backpack'].remove('dagger')

inventory['gold'] = 550
