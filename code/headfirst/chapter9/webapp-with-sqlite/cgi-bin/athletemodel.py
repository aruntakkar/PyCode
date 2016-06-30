import sqlite3

db_name = "coachdata.sqlite"


def get_names_from_store():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("""SELECT name FROM athletes""")
    response = [row[0] for row in results.fetchall()]
    connection.close()
    return(response)


def get_namesID_from_store():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("""SELECT name, id FROM athletes""")
    response = results.fetchall()
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
        """SELECT value name, dob FROM athletes WHERE id=?""", (athlete_id))
    (names, dob) = results.fetchone()
    # GET the list of Times from the timing_data
    results = cursor.execute(
        """SELECT FROM timing_data WHERE id=?""", (athlete_id))
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
