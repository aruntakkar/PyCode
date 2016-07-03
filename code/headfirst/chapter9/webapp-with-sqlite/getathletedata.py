import android
import json
import time

from urllib import urlencode
from urllib2 import urlopen

hello_msg = "Welcome to Coach Kelly's Timing App"

list_title = 'Here is your list of athletes:'

quit_msg = "Quitting Coach Kelly's App."

web_server = 'http://192.168.0.102:8080/'

get_names_cgi = '/cgi-bin/generate_names.py'

get_data_cgi = '/cgi-bin/generate_data.py'


def send_to_server(url, post_data=None):
    if post_data:
        page = urlopen(url, urlencode(post_data))
        print("if")
    else:
        page = urlopen(url)
        print("Else")
    return(page.read().decode("utf"))

app = android.Android()


def status_update(msg, how_long=2):
    app.makeToast(msg)
    time.sleep(how_long)

status_update(hello_msg)

athletes = sorted(json.loads(send_to_server(web_server + get_names_cgi)))

# Extract the athlete names only from the list of lists.
athlete_names = [ath[0] for ath in athletes]

app.dialogCreateAlert(list_title)

app.dialogSetSingleChoiceItems(athlete_names)

app.dialogSetPositiveButtonText('Select')

app.dialogSetNegativeButtonText('Quit')

app.dialogShow()

resp = app.dialogGetResponse().result

app.dailogCreateAlert(resp)

if resp['which'] in ('positive'):
    print(resp['which'])
    # when user taps the positive Button Work out
    # the element[0] from the list of result
    selected_athlete = app.dialogGetSelectedItems().result[0]
    print(selected_athlete)
    # look up the athlete_id associated with the selected athlete
    which_athlete = athletes[selected_athlete][1]
    print(which_athlete)
    # A web request to the server to Fetch the Athlete Data
    athlete = json.loads(send_to_server(
        web_server + get_data_cgi, {'which_athlete': which_athlete}))
    print(athlete)

    # Dynamically Create the dialog list
    athlete_title = athlete['Name'] + \
        ' (' + athlete['DOB'] + '), + top 3 times:'

    app.dialogCreateAlert(athlete_title)

    """
    This time user needs to see only
    the Data this time, so you need
    to See "dialogSetItems()"
    """

    app.dialogSetItems(athlete['top3'])

    app.dialogSetPositiveButtonText('OK')

    app.dialogShow()

    # wait for the User Response
    resp = app.dailogGetResponse().result

status_update(quit_msg)
