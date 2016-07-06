import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://placekitten.com/')
    kittens = response.read()
    print(kittens[559:1000])
except urllib.error.URLError as e:
    print('No kittez. Got an error code:', e)
