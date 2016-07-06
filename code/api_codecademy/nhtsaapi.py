from urllib2 import urlopen
from json import load

apiUrl = "http://www.nhtsa.gov/webapi/api/SafetyRatings"

# apiParam = "/modelyear/2013"
# apiParam = "/modelyear/2013/make/audi"
# apiParam = "/modelyear/2013/make/audi/model/a4"
apiParam = "/VehicleId/7045"

outputFormat = "?format=json"

response = urlopen(apiUrl + apiParam + outputFormat)

# code below is only to handle JSON response object/format
# use equivalent sets of commands to handle xml response object/format
json_obj = load(response)

# Load the Result (vehicle collection) from the JSON response
print '------------------------------'
print '           Result             '
print '------------------------------'
for objectCollection in json_obj['Results']:
    # Loop each vehicle in the vehicles collection
    for safetyRatingAttribute, safetyRatingValue in objectCollection.iteritems():
        print safetyRatingAttribute, ": ", safetyRatingValued

# After running this example, feel free to explore the results below
