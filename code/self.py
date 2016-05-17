class Restaurant(object):

    bankrupt = False

    def open_branch(self):
        if not self.bankrupt:
            print("branch opened")

x = Restaurant()
x.bankrupt
# The above command is same as Restaurant().bankrupt

"""
    As you see (self) refers to the bound variable or object, In
    First Case it refers to x because we assign restaurant class
    to x, whereas in the second case it referred to restaurant()
    Now if we have another Restaurant y, self will know to access
    the bankrupt value of y and not x
"""

y = Restaurant()
y.bankrupt = True
y.bankrupt


"""
    The first argument of every class method, including __init__, is
    always a reference to current instance of the class. By Convention
    the argument is always named self. In the __init__ method, self
    refers to newly created object, in other class methods, it refers to
    the instance whose method was called.
     * For example the below code is the same as above code
"""


class Restaurant(object):
    bankrupt = False

    def open_branch(this):
        if not this.bankrupt:
            print("branch opened")
