def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        else:
            return False
    else:
        return False
    # if year % 4 == 0 and year % 400 == 0:
        # return True
    # else:
        # return False
