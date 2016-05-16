import requests
from bs4 import BeautifulSoup


def get_product_info():
    url = "http://www.flipkart.com/all/~best-selling-mobile-laptop-accessories/pr?sid=all"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    for link in soup.findAll('a', {'class': 'pu-image'}):
        href = "http://flipkart.com" + link.get('href')
        get_single_item_data(href)


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    for item_name in soup.findAll('h1', {'class': 'title'}):
        print(item_name.string)

    for sellers_information in soup.findAll('a', {'class': 'seller-name'}):
        seller_name = sellers_information.string
        print(seller_name, " ", end="")

    for selling_information in soup.findAll('span', {'class': 'selling-price'}):
        selling_price = selling_information.string
        print(selling_price, " ", end="")

get_product_info()
