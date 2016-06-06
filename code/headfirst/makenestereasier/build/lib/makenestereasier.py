"""
    This is nester.py module, and it provides one function called print_lol(),
    which print lists that may or may not include nested
    lists.
"""


def print_lol(the_list, level=0):
    """
        This function takes a possitional argument "the_list",
        which is any Python list(of possibly nested list) Each
        data from nested list will be (recursively)printed to
        screen on its own line.

        A Second Argument called "level" is used to
        insert to tab-stops when a (nested-list) is encountered
    """
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, level+1)
        else:
            # Use the Value of "level" to Control how
            # Many tabs-stops are used.
            for tab_stop in range(level):
                print("\t", end="")
            print(each_item)
