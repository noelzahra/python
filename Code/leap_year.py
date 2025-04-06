# Testing #
from __future__ import print_function, division


def is_leap_year(year):
    year = int(year)

    if year % 100 != 0 and year % 4 == 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False

# y = 2000
# year_to_check = is_leap_year(y)
# print(f'Year is : {y}, {year_to_check}')

years = [2000, 2001, 2002, 2003, 2004]

for year in years:
    print(f'Year is: {year}, {is_leap_year(year)}')
