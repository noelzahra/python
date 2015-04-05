# Testing #
from __future__ import print_function


def is_leap_year(year):
    year = int(year)

    if year % 100 != 0 and year % 4 == 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False

year_to_check = is_leap_year(2000)

print(year_to_check)
