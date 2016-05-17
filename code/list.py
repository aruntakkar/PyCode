# Basic Example of List

# A list named player
players = [1, 2, 3, 4, 5, 6]

# print the list
print(players)

# Excess the element of list using the index like array
print(players[0])

print(players[1])

# Suppose you extend list player with the new data that list would be same
print(players + [5, 6, 7])
print(players)

# You can extend the list with append
players.append(120)
print(players)

# Extend the list with (list without name) here the list player would be same
Extended_players = players + [7, 8, 9, 10]
print(Extended_players)

# Slice the list upto index 2 (so element Till 2 will be given)
print(players[:2])

# To Add the element till index 2 element 0
players[:2] = [0, 0]
print(players)

# To Delete the element till the index 2
players[:2] = []

# print the list players with the deleted elements
print(players)

# To Empty the Whole list
players[:] = []
print(players)
