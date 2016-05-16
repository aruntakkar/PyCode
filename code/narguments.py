def addnumber(*args):
    total = 0
    for a in args:
        total += a
    print(total)

addnumber(3)
addnumber(3, 32)
addnumber(3, 43, 545, 234)
