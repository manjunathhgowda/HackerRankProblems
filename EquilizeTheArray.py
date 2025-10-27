'''
Equalize the Array

Given an array of integers, determine the minimum number of elements to delete
so that all remaining elements are equal.

Function Description
---------------------
Complete the function 'equalizeArray' below.

Parameters:
------------
int arr[n]: an array of integers

Returns:
---------
int: the minimum number of deletions required

Example:
---------
Input:
arr = [3, 3, 2, 1, 3]

Output:
2

Explanation:
------------
Delete 2 and 1 to leave [3, 3, 3].
This is minimal — deleting any other combination would require more deletions.

Constraints:
-------------
1 <= n <= 100
1 <= arr[i] <= 100
'''

def equalizeArray(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    max_count = max(freq.values())
    return len(arr) - max_count
print(equalizeArray([3, 3, 2, 1, 3]))  # Expected output: 2
print(equalizeArray([1, 2, 2, 3]))     # Expected output: 2
print(equalizeArray([4, 4, 4, 4]))     # Expected output: 0
