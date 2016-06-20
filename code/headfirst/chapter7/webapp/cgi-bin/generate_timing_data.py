#! /usr/local/bin/python3

import cgi
import athletemodel
import yate

athletes = athletemodel.get_from_store()

# which athlete data you are working with
# Web server send us the data to CGI Script(from genrate_list.py)
# Grab all the form data and put it in dictionary
form_data = cgi.FieldStorage()

athlete_name = form_data['which_athlete'].value

print(yate.start_response())

print(yate.include_header("Coach Kelly Timing Data"))

print(yate.header("Athlete: " + athlete_name + " " +
                  ', dob:' + athletes[athlete_name].dob + "."))

print(yate.para_text("The top Three times for the Athletes"))

print(yate.u_list(athletes[athlete_name].top3()))

print(yate.include_footer({"Home": "/index.html",
                           "Select another athlete:": "generate_list.py"}))
