
zoo_animals = {'Unicorn': 'Cotton Candy House', 'sloth': 'Rainforest Exhibit',
               'Bengal Tiger': 'Jungle House', 'Atlantic Puffin': 'Arctic Exhibit',
               'Rockhopper Penguin': 'Arctic Exhibit'}

# Removing the 'Unicorn' entry.
del zoo_animals['Unicorn']
del zoo_animals['sloth']
del zoo_animals['Bengal Tiger']

zoo_animals['Rockhopper Penguin'] = 'USA'

print(zoo_animals)
