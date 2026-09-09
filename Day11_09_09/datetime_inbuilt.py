# Notes: The datetime Module
#
# datetime is a built-in module used to work with dates and times,
# like getting the current date, formatting it, or creating a
# specific date or time.

from datetime import datetime, date, time

now = datetime.now()
print(now)
# datetime.now() gives the current date and time together, down to
# the microsecond

# date.today() gives only the current date, without the time part
# print(date.today())

# .time() on a datetime object gives only the time part, without the date
# print(datetime.now().time())

# date(year, month, day) creates a specific date of our own choosing
# print(date(2026, 1, 15))

# time(hour, minute, second) creates a specific time of our own choosing
# print(time(9, 35, 22))

# strftime() formats a datetime object into a readable string, using
# format codes, as shown in the table below
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%A, %B %d"))

# | Code | Meaning       |
# | ---- | ------------- |
# | %Y   | Year (2025)   |
# | %m   | Month (01-12) |
# | %d   | Day           |
# | %H   | Hour (24h)    |
# | %M   | Minutes       |
# | %S   | Seconds       |
# | %A   | Weekday name  |
# | %B   | Month name    |


# ------------------------------------------------------------
# Practice Questions
# ------------------------------------------------------------

# 1. Print the current date and time using datetime.now().

# 2. Print only today's date using date.today().

# 3. Create a date object for your own birthday, using date(year, month, day).

# 4. Print the current time using datetime.now().strftime(), showing
#    only hours, minutes and seconds.

# 5. Print the current date in the format DD-MM-YYYY using strftime().

# 6. Print the current day's weekday name (like "Monday") using
#    strftime() with %A.

# 7. Print the current date and time in the format:
#    "Today is <weekday name>, <month name> <day>, <year>"

# 8. Create a time object for 6:30 PM (18:30:00) using time(hour, minute, second).

# 9. Print the current month's name and the current year separately,
#    using two different strftime() calls.

# 10. Using datetime.now(), print the current date and time in three
#     different formats of your choice, using strftime().
