'''
HackerRank - Find the Median

Given an unsorted array with an odd number of integers,
find the median (middle element after sorting).

Steps:
1. Sort the array.
2. Median index = len(arr) // 2
3. Return arr[median_index]
'''

def findMedian(arr):
    arr.sort()
    mid = len(arr) // 2
    return arr[mid]


# -------- Example calls instead of main() --------

print(findMedian([0, 1, 2, 4, 6, 5, 3]))
# Output: 3

print(findMedian([5, 3, 1]))
# Output: 3

print(findMedian([9, 2, 7, 4, 6]))
# Output: 6
