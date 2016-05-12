# Basic Example of List

# A list named player
players = [1, 2, 3, 4, 5, 6]

# print the list
print(players)

# Excess the element of list using the index like array
print(players[0])

print(players[1])

# Extend the list with (list without name) here the list player would be same
Extended_players = players + [7, 8, 9, 10]
print(Extended_players)

# Excess the element upto index 2 (so element Till 2 will be given)
# So Here 2 is the endpoint
# gives the element from the list value 1,2
print(players[:2])

# To Delete the element till the index 2
# Create an empty list till the index you want to delete
players[:2] = []

# print the list players with the deleted elements
print(players)

# To Empty the Whole list
players[:] = []
print(players)
