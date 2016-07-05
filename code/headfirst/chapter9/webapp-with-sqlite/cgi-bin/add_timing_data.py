"""
    Script That Takes advantage of Python's built-in
    support for querying your CGI Script's environment
    using the os library, assuming enviorment values
    have been set by a friendly server.

    Note that data in the enviorment is available to
    your code as dictionary.
"""

# import cgi
# import os
# import time
# import sys
# import yate

# # Querying three enviornment variables and
# # assign their values to variables.

# print(yate.start_response('text/plain'))
# addr = os.environ['REMOTE_ADDR']
# host = os.environ['REMOTE_HOST']
# method = os.environ['REQUEST_METHOD']

# # Get the Current Time
# cur_time = time.asctime(time.localtime())

# # Display the queried data on standard error
# print(host + ", " + addr + ", " + cur_time + ": " +
#       method + ": ", end='', file=sys.stderr)

# form = cgi.FieldStorage()

# for each_form_item in form.keys():
#     print(each_form_item + '->' + form[each_form_item].value, end='',
#           file=sys.stderr)
# print(file=sys.stderr)
# print('OK')

import cgi
import sqlite3
import yate
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
db_name = os.path.join(BASE_DIR, "coachdata.sqlite")
print(db_name)

print(yate.start_response('text/plain'))

form_data = cgi.FieldStorage()
the_id = form_data['Athlete'].value
the_time = form_data['Time'].value

connection = sqlite3.connect(db_name)
cursor = connection.cursor()
cursor.execute(
    "INSERT INTO timing_data (athlete_id, value) VALUES (?, ?)", (the_id, the_time))
connection.commit()
connection.close()

print('OK')
