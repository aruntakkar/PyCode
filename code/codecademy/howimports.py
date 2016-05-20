# from math import sqrt
# print(sqrt(25))
import math  # import the math module
everything = dir(math)  # set everything to list of things from math
print(everything)

"""
    A Module is a file that contains definitions:- including variables and
    functions, that can use once it is imported
"""

"""
    We can import the module by
        import module_name
"""

"""
    it is possible to import only certain variables or functions from a given
    module, pulling it just a single function from module is (function import).
    it can be done by (from) keyword
        from module_name import function_name
        ex:- from math import sqrt
    Now we can just type sqrt() to get the square root of the number- no more
    math.sqrt()
"""

"""
    Universal imports :- what if we want all the variables and functions but
    don't want to have to constantly type math.?
    * Universal imports can handle this for
    from module_name import *
"""

"""
    Universal imports may look great on the surface, but they're not good they
    fill the program with the ton of variables and function name without the
    safety of those names still being associated with the module(s) they came
    from
"""

"""
    if you have function named sqrt and you import math, your function is safe,
    there is (math.sqrt) , if you do (from math import *) , however you have a
    problem, namely two d/w function with same name.
"""

"""
    if you do import * from several module at once, you won't be able to figure
    out which variable or function came from where.
"""

"""
    For this reason, its best to stick with either import module and type
    module.function_name or just import specific variables and functions from
    various modules as needed.
"""
