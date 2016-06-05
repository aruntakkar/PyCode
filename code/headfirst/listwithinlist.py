movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", [
    "Michael Palin", "John clesse", "Tarry Gilliam", "Eric Idle", "Tarry Jones"]]]

# for each_item in movies:
#     if isinstance(each_item, list):
#         for nested_item in each_item:
#             if isinstance(nested_item, list):
#                 for deeper_item in nested_item:
#                     print(deeper_item)
#             else:
#                 print(nested_item)
#     else:
#         print(each_item)


def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)


print_lol(movies)
