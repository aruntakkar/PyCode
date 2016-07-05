import sqlite3
import pickle
import os.path
from athletelist import AthleteList

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_name = os.path.join(BASE_DIR, "coachdata.sqlite")


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


def get_names_from_store():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("""SELECT name FROM athletes""")
    response = [row[0] for row in results.fetchall()]
    connection.close()
    return(response)


# In addition to the list of names,
# you need to extract an athlete's details from
# athletes table based on ID.
def get_athlete_from_id(athlete_id):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    # GET the Name and DOB From the athlete DB
    results = cursor.execute(
        """SELECT name, dob FROM athletes WHERE id=?""", (athlete_id))
    (name, dob) = results.fetchone()
    # GET the list of Times from the timing_data
    results = cursor.execute(
        """SELECT value FROM timing_data WHERE athlete_id=?""", (athlete_id))
    data = [row[0] for row in results.fetchall()]
    # Take the data from the both query results and turn it into a dictionary.
    response = {
        'Name': name,
        'DOB': dob,
        'data': data,
        'top3': data[0:3]
    }

    connection.close()
    return(response)


def get_namesID_from_store():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("""SELECT name, id FROM athletes""")
    response = results.fetchall()
    connection.close()
    return(response)
