
with open("james.txt") as jaf:
    data = jaf.readline()
james = data.strip().split(',')

with open('julie.txt') as jul:
    data = jul.readline()
Julie = data.strip().split(',')

with open('mikey.txt') as mil:
    data = mil.readline()
mikey = data.strip().split(',')

with open('sarah.txt') as sar:
    data = sar.readline()
sarah = data.strip().split(',')


print(sorted(james))
print(sorted(Julie))
print(sorted(mikey))
print(sorted(sarah))
