"""
    This is nester.py module, and it provides one function called print_lol(),
    which print lists that may or may not include nested
    lists.
"""


def print_lol(the_list, indent=False, level=0):
    """
        This function takes a possitional argument "the_list",
        which is any Python list(of possibly nested list) Each
        data from nested list will be (recursively)printed to
        screen on its own line.

        A Second Argument called "level" is used to
        insert to tab-stops when a (nested-list) is encountered

        Indent argument is used to set the priority for indention
        # if indent is (True) than make the indent.
        # if indent is (False) than not.
    """
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1)
        else:
            # specify when indenting is required by if condition
            if indent:
                # Use the Value of "level" to Control how
                # Many tabs-stops are used.
                for tab_stop in range(level):
                    print("\t", end="")
            print(each_item)
