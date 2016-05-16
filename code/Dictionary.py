# Keys and Values

classmates = {'Tony': 'cool but smells', 'Emma': 'sits behind me', 'lucy': 'she has too many Questions'}

# this will print the dictionary
# print(classmates)

# print the Value of particular key
# print(classmates['Tony'])

# dictionary consist of two item key, value
# items() loop through all the item in dictionary named classmates
for k, v in classmates.items():
    print(k + '\t' + v)
