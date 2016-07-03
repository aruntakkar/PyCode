# CGI script when called returns the data from get_names_from_store function
# in the JSON data Stream.

import sys
import json
import yate
import athletemodel

names = athletemodel.get_namesID_from_store()

print('The names are:' + names, file=sys.stderr)
print(yate.start_response("application/json"))
print(json.dumps(sorted(names)))
