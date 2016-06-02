# To read and write information to another file

"""
    This process is called file I/O ("stands for input/output")
"""

my_list = [i**2 for i in range(1, 11)]

# open this file in the write mode and store that result in a file object f

# r+ is used to read/write at same time

my_file = open("output.txt", "w")

for item in my_list:
    my_file.write(str(item) + "\n")

# we should close our file, if we don't close
# the file Python won't write to it properly.
my_file.close()

# to read the file
# r is used in open
# read() is used for reading


"""
    To Read the file line by line
    readline() is used
    if we open a file and call .readline() on
    file object, you will get the first line of the file
"""

file = open("text.txt", "w")
file.write("I'm the first line of the file!\n")
file.write("I'm the second line.\n")
file.write("Third line here, boss.\n")
file.close()

my_file = open("text.txt", "r")

print(my_file.readline())
print(my_file.readline())
print(my_file.readline())

my_file.close()

"""
    To flush the buffer in python close the file every time after read/write.
"""

"""
    there is option to automatically close the file
    with the keyword (with and as)
"""
with open("text.txt", "w") as textfile:
    textfile.write("Success!")
