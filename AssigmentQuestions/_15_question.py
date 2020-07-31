def leap_year(n):
    """
    In the Gregorian calendar, three criteria must be taken into account to identify leap years:
    The year must be evenly divisible by 4;
    If the year can also be evenly divided by 100, it is not a leap year; unless...
    The year is also evenly divisible by 400. Then it is a leap year.
    According to these rules, the years 2000 and 2400 are leap years,
    while 1800, 1900, 2100, 2200, 2300, and 2500 are not the leap years.
    """
    if not n % 400:
        return str(n) + " is a leap year"
    elif not n % 100:
        return str(n) + " is not a leap year"
    elif not n % 4:
        return str(n) + " is a leap year"
    else:
        return str(n) + " is not a leap year"


year = int(input("enter a year : "))
print(leap_year(year))
