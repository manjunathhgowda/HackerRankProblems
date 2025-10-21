#!/bin/python3
"""
Beautiful Days at the Movies

Given a range of days (i to j) and a divisor k, 
a day is considered "beautiful" if the absolute 
difference between the day number and its reverse 
is evenly divisible by k.

Example:
i = 20, j = 23, k = 6
Days: 20, 21, 22, 23
Beautiful days → 20 and 22 → Output: 2
"""

def beautifulDays(i, j, k):
    count = 0  # to count number of beautiful days
    for day in range(i, j + 1):  # iterate through each day in the range
        rev = int(str(day)[::-1])  # reverse the digits
        if abs(day - rev) % k == 0:  # check divisibility condition
            count += 1 
    return count
examples = [
    (20, 23, 6),   # Expected → 2
    (13, 45, 3),   # Expected → 33
    (1, 10, 2),    # Expected → 9
]

for i, j, k in examples:
    print(f"i={i}, j={j}, k={k} → {beautifulDays(i, j, k)}")

"""
Expected Output:
i=20, j=23, k=6 → 2
i=13, j=45, k=3 → 33
i=1, j=10, k=2 → 9
"""
