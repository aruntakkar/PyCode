a = 7890

"""
    When a Variable is declared inside a function it can't be used by another
    function only by that function(local Variables)
"""


def corn():
    a = 20
    print(a)


def fudge():
    print(a)

corn()
fudge()
