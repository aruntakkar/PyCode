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
