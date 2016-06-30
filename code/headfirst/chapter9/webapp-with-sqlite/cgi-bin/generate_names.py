# CGI script when called returns the data from get_names_from_store function
# in the JSON data Stream.

import json
import yate
import athletemodel

names = athletemodel.get_names_from_store()

print(yate.start_response("application/json"))
print(json.dumps(sorted(names)))
