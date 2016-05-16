import requests
from bs4 import BeautifulSoup


def story_extractor(href):
    source = requests.get(href)  # get the page containing the story
    plain_text = source.text  # save the plain text version of the source code in a variable
    # convert the source to a Beautiful Soup object
    soup = BeautifulSoup(plain_text, 'lxml')
    # find the <div> tag where the class is 'p'
    paragraph = soup.findAll('div', {'class': 'p'})
    story_text = str(paragraph)  # convert the story text found to a string
    # find the length of the story in characters to use in the next line
    length = len(story_text)
    # return the story minus the first and last characters which were square
    # brackets "[ ]"
    return story_text[1:length - 1]


def slashdot_crawler(pagesToCrawl):  # begin definition of slashdot_crawler function
    sd = open('slashdot.html', 'w')  # create html file to write stories to
    # write the initial HTML tags to the file to start the page
    sd.write('<html><head><title>Slashdot stories</title></head><body><h1>The latest Slashdot stories</h1><br>')
    page = 0  # initialize page to 0 since slashdot starts counting their pages at 0
    while page < pagesToCrawl:  # keep looping until we get to the defined number of pages to crawl
    print("Processing page " + str(page + 1) + " of " +
          str(pagesToCrawl) + "\n")  # prompt user on progress
    # assign the slashdot url to a variable
    url = "http://slashdot.org/?page=" + str(page)
    source = requests.get(url)  # get the source code of the page
    plain_text = source.text  # save the plain text version of the source code in a variable
    # convert the source to a Beautiful Soup object
    soup = BeautifulSoup(plain_text, 'lxml')
    # loop through all the <span> tags with their class = story-title
    for link in soup.findAll('span', {'class': 'story-title'}):
    href = link.a.get("href")  # get the link to the story
    title = link.a.string  # store the story title
    # print(title)
    #print('http:' + href)
    # print('\n')
    # for each story start a paragraph and create a link to the original story
    # using the story title
    sd.write('<p><a href="' + href + '">' + title + '</a><br>')
    # add "http:" to the beginning of the url since slashdot links start with
    # //
    story_link = "http:" + href
    # pass the link to the story extractor function which returns the actual
    # text content of the story
    story_contents = story_extractor(story_link)
    sd.write(story_contents)  # write the story content to the html file
    sd.write("</p><br>")  # close the html paragraph and insert a return
    page += 1  # increment page
    # once the loop exits, no more stories so we can close the html page
    sd.write('</body></html>')
    sd.close()  # close the html file we have been writing to

slashdot_crawler(3)  # call the function to crawl slashdot.org
print("Processing complete")  # prompt user to show that the program is done
