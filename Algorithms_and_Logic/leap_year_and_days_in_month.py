# FILE: leap_year_and_days_in_month.py
# CONCEPT: Modular Conditional Logic
# DEMONSTRATES: Using a helper function (is_leap_year) inside a main function (days_in_month) 
# to solve a complex conditional problem.

def is_leap_year(year):
    """Determines if a given year is a leap year using the official rules."""
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(month, year):
    """Returns the number of days in a given month, correctly accounting for leap years."""
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 31
        
# Note: Removed overly_complex_days_in_month as days_in_month is the cleaner implementation.
