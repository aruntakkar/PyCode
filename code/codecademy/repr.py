class Point3D(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    """
        One useful method to override is the built-in
        __repr()__ method, which is short for representation
        by providing a return value in this method, we can
        tell Python how to represent object of our class
    """

    def __repr__(self):
        return "(%s, %s, %s)" % (self.x, self.y, self.z)

my_point = Point3D(1, 2, 3)
print(my_point)
