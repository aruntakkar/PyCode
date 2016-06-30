import android
from urllib import urlencode
from urllib2 import urlopen

server_title = "which server should I use?"

server_msg = "Please Confirm the Server address/name to use for your athlete's timing data:"

timing_title = "Enter data"

timing_msg = "Provide a new timing value"

web_server = "http://192.168.0.102:8080/"

add_time_cgi = "/cgi-bin/add_timing_data.py"

app = android.Android()


def send_to_server(url, post_data=None):
    if post_data:
        page = urlopen(url, urlencode(post_data))
    else:
        page = urlopen(url)
    return(page.read().decode("utf8"))

app = android.Android()

# First dialog asks user to confirm the web address and port to use

resp = app.dialogGetInput(server_title, server_msg, web_server).result

# if user doesn't tap on the cancel button

if resp is not None:
    web_server = resp
    resp = app.dialogGetInput(timing_title, timing_msg).result
    # if user doesn't tap on the cancel button
    if resp is not None:
        new_time = resp
        send_to_server(web_server + add_time_cgi, {'TimingValue': new_time})
