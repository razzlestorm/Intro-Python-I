"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import argparse
import sys
import calendar
from datetime import datetime

def cal_func(month, year):
  if not month and not year:
    return calendar.TextCalendar().formatmonth(datetime.today().year, datetime.today().month)
  elif month and not year:
    month = int(month)
    year = datetime.today().year
  elif year and not month:
    month = datetime.today().month
    year = int(year)
  else:
    try:
      month = int(month)
#      cal = calendar.TextCalendar().formatmonth(year, month)
    except Exception as e:
      if e in (TypeError, NameError):
        month = datetime.today().month
    try:
      year = int(year)
    except Exception as e:
      if e in (TypeError, NameError, SyntaxError):
        year = datetime.today().year

  try:
    return calendar.TextCalendar().formatmonth(year, month)
  except Exception as e:
    print(e)
    print('Please make sure your input conforms to the following:')
    print('-m=int -y=int')

parser = argparse.ArgumentParser(description="""
                                 This program shows a text calendar
                                 for the month and year
                                 as set by the following arguments:
                                 By default, if no arguments are provided,
                                 it will return the current month's calendar.
                                 """)

parser.add_argument("--month", "-m", help="takes an integer, 0-12")
parser.add_argument("--year", "-y", help="takes an integer, any year")
month = parser.parse_args().month
year = parser.parse_args().year

print(cal_func(month, year))
