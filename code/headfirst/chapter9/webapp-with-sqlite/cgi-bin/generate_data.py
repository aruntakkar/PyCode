# Here's the Code for the cgi-bin/generate_data.py
# CGI Script which takes a web request and returns the
# indicated athlete's data from model

import cgi
import json
import athletemodel
import yate

form_data = cgi.FieldStorage()

athlete_id = form_data['which_athlete'].value

athlete = athletemodel.get_athlete_from_id(athlete_id)

print(yate.start_response('application/json'))

print(json.dumps(athlete))
