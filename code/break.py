# number divisble by 4 upto 100
for x in range(101):
    if x % 4 == 0:
        print(x)

magicnumber = 26

for n in range(101):
    if n is magicnumber:
        print(n, "is the magic number")
        break
    else:
        print(n)
