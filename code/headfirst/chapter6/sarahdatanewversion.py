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

        # creating the temp list to hold the list untill dictionary
        temp1 = data.strip().split(",")

        # return the dictionary by key/value mapping of the list data.
        return {'Name': temp1.pop(0),
                'DOB':  temp1.pop(0),
                'Times': str(sorted(set([sanitize(t) for t in temp1]))[0:3])}

    except IOError as err:
        print("File error " + str(err))

# Invoking the read_files with the filename attribute

james = read_files('james2.txt')
julie = read_files('julie2.txt')
mikey = read_files('mikey2.txt')
sarah = read_files('sarah2.txt')

# Printing the athletes name and there respective names

print(james['Name'] + " Fastest times are " + james['Times'])

print(julie['Name'] + " Fastest times are " + julie['Times'])

print(mikey['Name'] + " Fastest times are " + mikey['Times'])

print(sarah['Name'] + " Fastest times are " + sarah['Times'])
