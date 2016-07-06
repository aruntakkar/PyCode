# ######### Example request #############
# POST /learn-http HTTP/1.1
# Host: www.codecademy.com
# Content-Type: text/html; charset=UTF-8
# Name=Eric&Age=26

import requests

body = {'Name': 'Eric', 'Age': '26'}

# Make the POST request here, passing body as the data:
response = requests.post("http://codecademy.com/learn-http/", data=body)

print(response)
