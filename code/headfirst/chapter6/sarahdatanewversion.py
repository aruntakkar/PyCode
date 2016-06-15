def sanitize(time_string):
    if ":" in time_string:
        splitter = ":"
    elif "-" in time_string:
        splitter = "-"
    else:
        return time_string

    (mins, secs) = time_string.split(splitter)
    return (mins + "." + secs)


def get_coach_data(filename):

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

# Invoking the get_coach_data function with the files

james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')

# Printing the athletes name and there respective names

print(james['Name'] + " Fastest times are " + james['Times'])

print(julie['Name'] + " Fastest times are " + julie['Times'])

print(mikey['Name'] + " Fastest times are " + mikey['Times'])

print(sarah['Name'] + " Fastest times are " + sarah['Times'])
