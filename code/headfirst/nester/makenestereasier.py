"""
    This is nester.py module, and it provides one function called print_lol(),
    which print lists that may or may not include nested
    lists.
"""


def print_lol(the_list):
    """
        This function takes a possitional argument "the_list", which is any
        Python list(of possibly nested list) Each
        data from nested list will be (recursively)
        printed to screen on its own line.
    """
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)
