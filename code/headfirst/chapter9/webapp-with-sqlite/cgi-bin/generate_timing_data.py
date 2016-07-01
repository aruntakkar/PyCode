#! /usr/local/bin/python3

import cgi
import athletemodel
import yate

form_data = cgi.FieldStorage()

# Access the named piece of data from the form's data.
athlete_id = form_data['which_athlete'].value

athletes = athletemodel.get_athlete_from_id(athlete_id)

# Here cgi module is used to access the form data coming from genrate_list.py
# which athlete data you are working with
# Web server send us the data to CGI Script(from genrate_list.py)
# Grab all the form data and put it in dictionary


print(yate.start_response())

print(yate.include_header("NUAC's Timing Data"))

print(yate.header("Athlete: " + athletes['Name'] + " " +
                  ', DOB:' + athletes['DOB'] + "."))

print(yate.para_text("The Top Three times for the Athletes are:"))

print(yate.u_list(athletes['top3']))

print(yate.para_text("The entire set of timing data is: " +
                     str(athletes['data']) + " (duplicates removed)."))

print(yate.include_footer({"Home": "/index.html",
                           "Select another athlete": "generate_list.py"}))
