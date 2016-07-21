from find_it import find_closest
from tm2secs2tm import time2secs, secs2time

""" find_nearest_time Takes two arguments, the time
    to look for and a list of times to search, The
    function returns the closest time found as a string:"""


def find_nearest_time(look_for, target_data):
    """ Convert the time string you are looking
    for into its equivalent value in seconds"""

    what = time2secs(look_for)

    # Convert line of time strings into seconds:

    where = [time2secs(t) for t in target_data]

    """Call "find_closest()" supplying the converted data: """

    res = find_closest(what, where)
    return(secs2time(res))

# For Checking Purpose
print(find_nearest_time(
    '59:59', ['56:29', '57:45', '59:03', '1:00:23', '1:01:45']))
