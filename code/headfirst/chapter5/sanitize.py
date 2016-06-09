with open("james.txt") as jaf:
    data = jaf.readline()
james = data.strip().split(',')

with open('julie.txt') as jul:
    data = jul.readline()
julie = data.strip().split(',')

with open('mikey.txt') as mil:
    data = mil.readline()
mikey = data.strip().split(',')

with open('sarah.txt') as sar:
    data = sar.readline()
sarah = data.strip().split(',')


def sanitize(time_string):
    # use of in to check if the string contains a dash or colon.
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    # do nothing if string don't need to be sanitized.
    else:
        return time_string

    # split the string to extract the minutes and seconds parts.
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)


# lists to contain the sanitize data of athletes
clean_James = []
clean_Julie = []
clean_Mikey = []
clean_Sarah = []

# iterating over the each list and sanitizing the data.
for each_t in james:
    clean_James.append(sanitize(each_t))

for each_t in julie:
    clean_Julie.append(sanitize(each_t))

for each_t in mikey:
    clean_Mikey.append(sanitize(each_t))

for each_t in sarah:
    clean_Sarah.append(sanitize(each_t))

print(sorted(clean_James))
print(sorted(clean_Julie))
print(sorted(clean_Mikey))
print(sorted(clean_Sarah))
