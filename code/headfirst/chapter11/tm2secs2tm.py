import time


# The function ensures that all times are formatted in "HH:MM:SS" format.
# This helps keep things simple when doing conversions to seconds.
def format_time(time_string):
    tlen = len(time_string)
    if tlen < 3:
        original_format = '%S'
    elif tlen < 6:
        original_format = '%M:%S'
    else:
        original_format = '%H:%M:%S'
    # strftime():- Convert time tuple to string according to format spec.
    # strptime():- Parse time tuple to string according to format spec.
    time_string = time.strftime(
        '%H:%M:%S', time.strptime(time_string, original_format))
    return(time_string)


# Given a time string Convert it to a value in seconds.
def time2secs(time_string):
    time_string = format_time(time_string)
    (hours, mins, secs) = time_string.split(':')
    seconds = int(secs) + (int(mins) * 60) + (int(hours) * 60 * 60)
    return(seconds)


# Convert a value in seconds to a "time string"
def secs2time(seconds):
    return(time.strftime(time.strftime('%H:%M:%S', time.gmtime(seconds))))
