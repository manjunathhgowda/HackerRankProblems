#!/bin/python3

'''
Question:
Given an array of integers and a positive integer k, determine the number of pairs (i, j) where:
- i < j
- (ar[i] + ar[j]) is divisible by k

Example:
ar = [1, 3, 2, 6, 1, 2], k = 3

Valid pairs:
(0, 2) → 1+2 = 3
(0, 5) → 1+2 = 3
(1, 3) → 3+6 = 9
(2, 4) → 2+1 = 3
(4, 5) → 1+2 = 3

Total = 5

Function Description:
Complete the 'divisibleSumPairs' function below.

Parameters:
    n: INTEGER → size of array
    k: INTEGER → divisor
    ar: INTEGER_ARRAY → array of integers

Returns:
    INTEGER → number of valid pairs
'''


def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count
print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))
