def remove_duplicates(Previouslist):
    clear_list = []
    for item in Previouslist:
        if item not in clear_list:
            clear_list.append(item)
    print(clear_list)
    return clear_list

remove_duplicates([1, "arun", "arun", 2, 2])
