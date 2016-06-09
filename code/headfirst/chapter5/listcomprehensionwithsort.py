# with open('james.txt') as jam:
#     data = jam.readline()
# james = data.strip().split(',')

# with open('julie.txt') as jul:
#     data = jul.readline()
# julie = data.strip().split(',')

# with open('mikey.txt') as mik:
#     data = mik.readline()
# mikey = data.strip().split(',')

# with open('sarah.txt') as sar:
#     data = sar.readline()
# sarah = data.strip().split(',')


# Function to remove the read the files
def read_files(file_name):
    try:
        with open(file_name) as file:
            data = file.readline()
        return (data.strip().split(','))
    except IOError as err:
        print("File Error " + err)
        return none

james = read_files('james.txt')
julie = read_files('julie.txt')
mikey = read_files('mikey.txt')
sarah = read_files('sarah.txt')


# function to check the string is containing (:) or (-)
def sanitize(time_string):
    if ':' in time_string:
        spliter = ':'
    elif '-' in time_string:
        spliter = '-'
    else:
        return time_string

    (mins, secs) = time_string.split(spliter)
    return (mins + '.' + secs)

# other way of remove the duplicates is using the sets
print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])


# Function to get the data with duplicates from lists not repeatable code
# def remove_duplicates(list_name):
#     unique_list = []
#     for each_t in list_name:
#         if each_t not in unique_list:
#             unique_list.append(each_t)
#     print(unique_list[0:3])

# remove_duplicates(clean_james)
# remove_duplicates(clean_julie)
# remove_duplicates(clean_mikey)
# remove_duplicates(clean_sarah)


# removing the duplicates by iteration

# unique_james = []
# for each_t in clean_james:
#     if each_t not in unique_james:
#         unique_james.append(each_t)
# print(unique_james[0:3])

# unique_julie = []
# for each_t in clean_julie:
#     if each_t not in unique_julie:
#         unique_julie.append(each_t)
# print(unique_julie[0:3])

# unique_mikey = []
# for each_t in clean_mikey:
#     if each_t not in unique_mikey:
#         unique_mikey.append(each_t)
# print(unique_mikey[0:3])

# unique_sarah = []
# for each_t in clean_sarah:#     if each_t not in unique_sarah:
#         unique_sarah.append(each_t)
# print(unique_mikey[0:3])
