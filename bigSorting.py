'''
Big Sorting

Consider an array of numeric strings where each string is a positive number with anywhere 
from 1 to 10^6 digits. Sort the array's elements in non-decreasing (ascending) order 
based on their integer values.

Function Description:
----------------------
Complete the function 'bigSorting' below.

Parameters:
------------
string unsorted[n]: an unsorted array of integers as strings

Returns:
---------
string[n]: the array sorted in numerical order

Example:
---------
Input:
unsorted = ['31415926535897932384626433832795', '1', '3', '10', '3', '5']

Output:
['1', '3', '3', '5', '10', '31415926535897932384626433832795']

Explanation:
------------
When we sort these numbers by their actual integer value (not string order), we get
the above result.

Constraints:
------------
1 <= n <= 2 * 10^5
Each number has no leading zeros and may contain up to 10^6 digits.
The total number of digits across all numbers ≤ 10^6.
'''

def bigSorting(unsorted):
    # Sort first by length, then lexicographically
    unsorted.sort(key=lambda x: (len(x), x))
    return unsorted


# Example test cases (like HackerRank custom input)
print(bigSorting([
    '31415926535897932384626433832795',
    '1',
    '3',
    '10',
    '3',
    '5'
]))
# Expected: ['1', '3', '3', '5', '10', '31415926535897932384626433832795']

print(bigSorting([
    '1',
    '2',
    '100',
    '12303479849857341718340192371',
    '3084193741082937',
    '3084193741082938',
    '111',
    '200'
]))
# Expected: ['1', '2', '100', '111', '200', '3084193741082937', '3084193741082938', '12303479849857341718340192371']
