# ################# Example response ##########################
# HTTP/1.1 200 OK
# Content-Type: text/xml; charset=UTF-8

# <?xml version="1.0" encoding="utf-8"?>
# <string xmlns="http://www.codecademy.com/">Accepted</string>
##############################################################

import requests
response = requests.get("http://placekitten.com/")

# print the header information from the response
print(response.headers)
