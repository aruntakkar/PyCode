# Here's the Code for the cgi-bin/generate_data.py
# CGI Script which takes a web request and returns the
# indicated athlete's data from model

# ! usr/local/bin/python3

import cgi
import json
import athletemodel
import yate

athletes = athletemodel.get_from_store()

form_data = cgi.FieldStorage()

athlete_name = form_data['which_athlete'].value

print(yate.start_response('application/json'))

print(json.dumps(athletes[athlete_name].as_dict))
