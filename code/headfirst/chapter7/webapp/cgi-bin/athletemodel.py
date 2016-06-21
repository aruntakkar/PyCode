import pickle
from athletelist import AthleteList


def get_coach_data(filename):
    try:
        with open(filename) as file:
            data = file.readline()
        temp1 = data.strip().split(",")

        return(AthleteList(temp1.pop(0), temp1.pop(0), temp1))

    except IOError as err:
        print("File error (get_coach_data): " + str(err))


def put_to_store(files_list):
    all_athletes = {}

    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath

    try:
        with open("athletes.pickle", "wb") as atpf:
            pickle.dump(all_athletes, atpf)

    except IOError as err:
        print("File error(put_and_store):" + str(err))

    return(all_athletes)


def get_from_store():
    all_athletes = {}

    try:
        with open("athletes.pickle", "rb") as atpf:
            all_athletes = pickle.load(atpf)
    except IOError as err:
        print("File error (get_from_store): " + str(err))

    return(all_athletes)


# the_files = ['sarah2.txt', 'james2.txt', 'mikey2.txt', 'julie2.txt']

# data = put_to_store(the_files)

# print("-To Access the data, Use the dictionary returned by put_to_store()-")

# for each_athlete in data:
#     print(data[each_athlete].name + ' ' +
#           data[each_athlete].dob)

# print("-To Checking the get_from_store() functionality to unpickle the data-")

# data_copy = get_from_store()

# for each_athlete in data_copy:
#     print(data_copy[each_athlete].name + ' ' + data_copy[each_athlete].dob)
