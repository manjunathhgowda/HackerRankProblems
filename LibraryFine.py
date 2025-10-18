'''
Your local library needs your help! 
Given the expected and actual return dates for a library book, 
create a program that calculates the fine (if any).

The fee structure is as follows:

1 If the book is returned on or before the expected return date → no fine.
2 If the book is returned after the expected return day but still within 
    the same month and year → 15 Hackos × number of late days.
3 If the book is returned after the expected return month but still within 
    the same year → 500 Hackos × number of late months.
4 If the book is returned after the expected year → fixed fine of 10000 Hackos.

Charges are based only on the least precise measure of lateness.
Example:
Returned: 9 6 2015
Due:      6 6 2015

Same month and year, 3 days late → fine = 15 × 3 = 45 Hackos.

Sample Input:
9 6 2015
6 6 2015

Sample Output:
45
'''

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Case 1: Returned on or before due date → no fine
    if (y1 < y2) or (y1 == y2 and m1 < m2) or (y1 == y2 and m1 == m2 and d1 <= d2):
        return 0
    if y1 == y2 and m1 == m2:   # Case 2: Returned late within same month and year
        return 15 * (d1 - d2)
    if y1 == y2:                # Case 3: Returned late within same year
        return 500 * (m1 - m2)
    if y1 > y2:                 # Case 4: Returned in a later year
        return 10000
d1, m1, y1 = 9,6,2015
d2, m2, y2 = 6,6,2015
print(libraryFine(d1, m1, y1, d2, m2, y2))
