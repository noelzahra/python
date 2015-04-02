# Testing #
from math import floor

def is_leap_year(year):
    year = int(year)

    if year % 100 != 0 and year % 4 == 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True

print(2014)
