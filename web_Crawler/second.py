Description:
    # this program goes on website
    # https://www.thenewboston.com/search.phptype=0&sort=reputation ,and goes
    # on every user's profile, and on that profile, it prints the first few
    # (approx. 20) links of latest photos. To view photos, click on url or
    # copy in web broser.


import requests
from bs4 import BeautifulSoup


# this function gets links to user's profiles
def trade_spider(max_pages):
page = 1
while page <= max_pages:
url = 'https://www.thenewboston.com/search.phptype=0&sort=reputation&page==' + \
    str(page)
source_code = requests.get(url, allow_redirects=False)
plain_text = source_code.text.encode('ascii', 'replace')
# soup = BeautifulSoup(plain_text) #this line causes error! (uncomment, to
# learn new things)
soup = BeautifulSoup(plain_text, 'html.parser')
for link in soup.findAll('a', {'class': 'user-name'}):  # all profiles
print(' <<---BEGINNING OF LINK--->>')
print('link: ', link)
href = link.get('href')
title = link.string
print('href: ', href)
print('title: ', title)
get_single_item_data(href)    # comment this for better understanding
print(' <<---END OF link--->>')
print('page: ', page)
page += 1


# I am now on user's profile and I now print links to users's photos
def get_single_item_data(item_url):

print(' <<--- BEGINNING OF get_single_item_data() --->>')
source_code = requests.get(item_url)
plain_text = source_code.text
# soup = BeautifulSoup(plain_text) #this causes error!! (uncomment, to
# learn new things)
soup = BeautifulSoup(plain_text, "lxml")  # use this line, to avoid error!!
# all photos of the user
for item_name in soup.findAll('img', {'class': 'img-responsive'}):
print('item_name :', item_name)
photo = 'https://www.thenewboston.com' + item_name.get('src')
print('Click the link to open the photo: ', photo)
print(' <<--- END OF get_single_item_data() --->>')

trade_spider(1)
