import requests
from bs4 import BeautifulSoup


# maximum of pages in forum, number of tutorial
def code_spider(max_pages, ttnr, specifier):
    dest_url = 'source' + str(ttnr) + '_' + specifier + '.py'
    page = 1
    done = False
    no = ttnr
    while page <= max_pages:
        url = 'https://www.thenewboston.com/forum/category.php?id=15&orderby=recent&page=' + \
            str(page)
        source_code = requests.get(url)  # holt den source code
        plain_text = source_code.text  # verwandelt sc in plain text
        # laedt den plain text in ein bs objekt
        soup = BeautifulSoup(plain_text, "html.parser")
        # loop thru source and find links(a) with the 'class' of 'ad-title'
        for link in soup.findAll('a', {'class': 'post-title'}):
            href = 'https://www.thenewboston.com' + link.get('href')
            title = link.string  # takes the string value
            if title[0:46] == '[source code] Python Programming Tutorial - ' + str(ttnr):
                print(title)
                print(href)
                done = True
                break
        if done:
            code_getter(href, dest_url)
            break
        page += 1


def code_getter(code_url, rl):
    codeExtract = requests.get(code_url)
    plainText = codeExtract.text
    soup = BeautifulSoup(plainText, "html.parser")
    fx = open(rl, "w")
    for results in soup.find('code'):
        resultLine = str(results).replace('<br>', '\n').replace(
            "\ufffd", '  ').replace('&l_t_;', '<').replace('</br>', '')
        fx.write(resultLine + "\n")
    fx.close()

code_spider(20, 25, 'web_crawler')
