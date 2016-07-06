import requests

response = requests.get('http://placekitten.com/')

print(response.status_code)
