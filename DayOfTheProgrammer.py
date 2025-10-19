"""
Day of the Programmer

Marie invented a Time Machine and wants to test it by time-traveling to visit Russia on the Day of the Programmer (the 256th day of the year)
during a year in the inclusive range from 1700 to 2700.

Rules:
- From 1700 to 1917, Russia used the Julian calendar.
- From 1919 onward, Russia used the Gregorian calendar.
- In 1918, the transition occurred: after January 31st came February 14th.
  So February had only 15 days that year.

Leap Year Rules:
- Julian calendar: year % 4 == 0
- Gregorian calendar: (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

Task:
Given a year, find the date of the 256th day of that year (Day of the Programmer)
and print it in the format dd.mm.yyyy

Examples:
----------
Input: 2017  → Output: 13.09.2017
Input: 2016  → Output: 12.09.2016
Input: 1800  → Output: 12.09.1800
"""

def dayOfProgrammer(year):
    # Special case: transition year
    if year == 1918:
        return "26.09.1918"  # February lost 13 days, so the 256th day shifted

    # Julian calendar (<= 1917)
    elif year < 1918:
        if year % 4 == 0:
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"

    # Gregorian calendar (>= 1919)
    else:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"

examples = [2017, 2016, 1800, 1918, 2000, 2100]
for y in examples:
    print(dayOfProgrammer(y))
