def median(numberlist):
    numberlist = sorted(numberlist)

    if len(numberlist) % 2 == 0:

        first_element_index = len(numberlist) / 2.0

        first_element = numberlist[int(first_element_index)]

        print(first_element)

        second_element_index = first_element_index - 1

        second_element = numberlist[int(second_element_index)]

        print(second_element)

        median_of_odd_list = (first_element + second_element) / 2.0

        print("median of odd list:", median_of_odd_list)

        return median_of_odd_list

    else:
        median_element_index = len(numberlist) / 2.0

        print(median_element_index)

        median_of_even_list = numberlist[int(median_element_index)]

        print("median of even list:", median_of_even_list)

        return median_of_even_list

median([5, 2, 3, 1, 4, 6, 7])
