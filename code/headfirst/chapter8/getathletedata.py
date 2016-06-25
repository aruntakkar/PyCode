import android
import json
import time

from urllib import urlencode
from urllib2 import urlopen

hello_msg = "Welcome to Coach Kelly's Timing App"

list_title = 'Here is your list of athletes:'

quit_msg = "Quitting Coach Kelly's App."

web_server = 'http://192.168.0.101:8080/'

get_names_cgi = '/cgi-bin/generate_names.py'

get_data_cgi = '/cgi-bin/generate_data.py'


def send_to_server(url, post_data=None):
    if post_data:
        page = urlopen(url, urlencode(post_data))
    else:
        page = urlopen(url)
    return(page.read().decode("utf8"))

app = android.Android()


def status_update(msg, how_long=2):
    app.makeToast(msg)
    time.sleep(how_long)

status_update(hello_msg)

athlete_names = sorted(json.loads(send_to_server(web_server + get_names_cgi)))

app.dialogCreateAlert(list_title)

app.dialogSetSingleChoiceItems(athlete_names)

app.dialogSetPositiveButtonText('Select')

app.dialogSetNegativeButtonText('Quit')

app.dialogShow()

resp = app.dialogGetResponse().result

# To Know the Which button is pressed
if resp['which'] in ('positive'):
    # when user taps the possitive Button Work out
    # the index value
    selected_athlete = app.dialogGetSelectedItems().result[0]

    # look up the athlete_name using the index value
    which_athlete = athlete_names[selected_athlete]

    # A web request to the server to Fetch the Athlete Data
    athlete = json.loads(send_to_server(
        web_server + get_data_cgi, {'which_athlete': which_athlete}))

    # Dynamically Create the dialog list
    athlete_title = athlete['name'] + \
        ' (' + athlete['DOB'] + '), + top 3 times:'

    app.dialogCreateAlert(athlete_title)

    """
    This time user needs to see only
    the Data this time, so you need
    to See "dialogSetItems()"
    """

    app.dialogSetItems(athlete['Top3'])

    app.dialogSetPositiveButtonText('OK')

    app.dialogShow()

    # wait for the User Response
    resp = app.dailogGetResponse().result

status_update(quit_msg)
