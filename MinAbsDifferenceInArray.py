"""
Minimum Absolute Difference in an Array

Given an array of integers, find the minimum absolute difference between
any two elements.

Example:
---------
arr = [3, -7, 0]

All possible pairs and their absolute differences:
|3 - (-7)| = 10
|3 - 0| = 3
|-7 - 0| = 7

The minimum absolute difference is 3.

Function Description:
---------------------
minimumAbsoluteDifference(arr)
    - arr: list of integers
Returns:
    - Integer: the smallest absolute difference between any two elements

Optimal Logic:
--------------
- Sorting the array allows us to find the smallest difference between 
  consecutive elements (since the closest numbers will have the smallest difference).
- This reduces the time complexity from O(n²) → O(n log n).

Example:
---------
Input:
3
3 -7 0
Output:
3
"""

def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff=[]
    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i + 1])
        min_diff.append(diff)
    return min(min_diff)

examples = [
    [3, -7, 0],                             # Expected output: 3
    [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75],  # Expected output: 1
    [1, -3, 71, 68, 17]                     # Expected output: 3
]
for arr in examples:
    print(minimumAbsoluteDifference(arr))