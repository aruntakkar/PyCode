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


sarah = read_files('sarah2.txt')

# dictionary approach to mapping(associate) the data values with key

sarah_data = {}
sarah_data['Name'] = sarah.pop(0)
sarah_data['DOB'] = sarah.pop(0)
sarah_data['Times'] = sarah

print(sarah_data['Name'] + " Fastest times are " +
      str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))
