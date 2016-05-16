import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://buckysroom.org/trade/search.php?page=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('a', {'class': 'item-name'}):
            href = "http://www.buckysroom.org" + link.get('href')
            # title = link.string
            # print(title)
            # print(href)
            get_single_item_data(href)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for item_name in soup.findAll('div', {'class': 'i-name'}):
        print(item_name.string)
    for link in soup.findAll('a'):
        href = "https://buckysroom.org" + link.get('href')
        print(href)

trade_spider(1)
