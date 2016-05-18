import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    for post_text in soup.findAll('a', {'class': 'title'}):
        content = post_text.string
        # split the sentence on Basis of the spaces with all letter lower cased
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)


def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*()_+'\"<>?,./;'[]-=|"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)
        numbers = "1234567890"
        for i in range(0, len(numbers)):
            word = word.replace(numbers[i], "")
        if len(word) > 0:
            # print(word)
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    """
        Sort the Dictionary for higher value words in the list
        Sorted Takes two parameters one is what to sort, How to Sort
        (what you wanna sort) By
    """
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)

start('https://thenewboston.com/forum/category.php?id=15')
