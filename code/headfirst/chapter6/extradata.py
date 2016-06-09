def sanitize(time_string):
    if ":" in time_string:
        splitter = ":"
    elif "-" in time_string:
        splitter = "-"
    else:
        return time_string

    (mins, secs) = time_string.split(splitter)
    return (mins + "." + secs)


def read_files(filename):
    try:
        with open(filename) as file:
            data = file.readline()
        return (data.strip().split(","))
    except IOError as err:
        print("File error " + str(err))


# spliting the data according to updated data
sarah = read_files('sarah2.txt')
# calls to pop(0) return and removes the data from front of the list
# Two calls to pop(0) remove the first two data values and assignes them.
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
print(sarah_name + " fastest times are: " +
      str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
