import datetime

# now using a function called datetime.now to retrive current date and time

now = datetime.datetime.now()

# if we don't want the entire date

current_year = now.year

current_month = now.month

current_day = now.day

print(now)

print(current_day)

print(current_month)

print(current_year)

"""
 if you want date in mm/dd/yy format use string substiution again, Remember
 that the % operator will fill %s placeholder in the string on the left with
 the strings in the parantheses on the right.
"""
today_date = datetime.datetime.now()

# print in specific format month/day/year format

print('%s/%s/%s' % (today_date.day, today_date.month, today_date.year))
