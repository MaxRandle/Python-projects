"""
This program determines
the day of the week for any given date.

The script uses an alorithm which uses integer (floor) division,
this means that only if the year is divisible by exactly 4, will the
program conpensate for leapyears.
"""
def daycalc(day, month, year):
    """
    Arguments:
        day - the day of the month (1-31)
        month - the month of the year (1-12)
        year - the year
    Returns:
        the day of the week

    test
    >>> daycalc(25, 8, 2013)
    'Sunday'
    >>> daycalc(8, 12, 1979)
    'Saturday'
    >>> daycalc(1, 1, 2142)
    'Monday'
    """

    a = (14 - month)//12
    y = year - a
    m = month + 12*a - 2
    d = (day + y + y//4 - y//100 + y//400 + (31*m)//12) % 7

    if d == 0:
        x = ("Sunday")

    if d == 1:
        x = ("Monday")
    
    if d == 2:
        x = ("Tuesday")
    
    if d == 3:
        x = ("Wedensday")
    
    if d == 4:
        x = ("Thursday")
    
    if d == 5:
        x = ("Friday")
    
    if d == 6:
        x = ("Saturday")
    return x
       
import doctest
doctest.testmod()
