from xml.dom import minidom

f = open('pets.txt', 'r')
pets = minidom.parseString(f.read())
print(pets)
f.close()

names = pets.getElementsByTagName('name')
print(names)
for name in names:
    print(name.firstChild.nodeValue)
