# Find Friday the 13ths (Difficulty 8 out of 10)
# Create a function that given a year, returns every month that had/has a Friday the 13th.

# Your function should return a list of month names.

from datetime import date
import calendar

def unlucky_months(year):
    sequence = []
    for month in range(1, 13):
        if date(year, month, 13).weekday() == 4:
            sequence.append(calendar.month_name[month])
    return sequence

user_input = int(input("What year are we looking at? "))
print(unlucky_months(user_input))