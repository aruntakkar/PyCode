# To Access the element in the list
item = ['May 18 2016', 'Python Books', 557]
print(item[1])

# if list is same size unpacking of list in variables to better access
date, item, price = ['May 18 2016', 'Python Books', 557]
print(date)


# if list is not equal size use * symbol to inculude many values in 1 variable
def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([10, 20, 30, 40, 50])
