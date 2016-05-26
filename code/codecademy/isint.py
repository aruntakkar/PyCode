def is_int(x):
    absolutecount = abs(x)
    typecount = type(x)
    roundcount = round(absolutecount)
    if typecount and absolutecount - roundcount == 0:
        print(True)
        return True
    else:
        print(False)
        return False

is_int(7.0)
