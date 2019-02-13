#!/usr/bin/env python3
# function to compute if a given year is a leap year or not.
# A leap year is defined as:
#   A year which is divisible by four,
#   except if divisible by 100,
#   unless divisible by 400.


def is_leap_year(year):
    # a one-liner solution
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    # my first attempt:
    # if year % 4 == 0:
        # if year % 100 == 0:
            # if year % 400 == 0:
                # return True
            # return False
        # else:
            # return True
        # return True
    # else:
        # return False
