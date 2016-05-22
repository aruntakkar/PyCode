# function can take list as an input and perform various operations on that.


def count_small(numbers):
    total = 0
    for n in numbers:
        if n < 10:
            total = total + 1
    return total

lost = [4, 8, 15, 16, 23, 42]
small = count_small(lost)
print(small)


def fizz_count(x):
    count = 0
    for item in x:
        if item == "fizz":
            count = count + 1
    return count

list = ["fizz", "cat", "fizz"]
result = fizz_count(list)
print(result)

# string are also like list with characters as elements

word = "Programming is Fun"

for letter in word:
    print(letter)
