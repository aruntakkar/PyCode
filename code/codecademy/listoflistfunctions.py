n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]


def flatten(lists):
    results = []
    for lst in lists:
        for number in lst:
            print(number)
            results.append(number)
    return results

print(flatten(n))
