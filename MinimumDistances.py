'''Minimum Distances

The distance between two array values is the number of indices between them.  
Given an array `a`, find the minimum distance between any pair of equal elements.  
If no such pair exists, return -1.

Function Description
---------------------
Complete the function 'minimumDistances' below.

Parameters:
------------
int a[n]: an array of integers

Returns:
---------
int: the minimum distance found, or -1 if there are no matching elements.

Example:
---------
Input:
a = [7, 1, 3, 4, 1, 7]

Output:
3

Explanation:
------------
There are two pairs to consider:
- The 1's are at indices 1 and 4 → distance = 3  
- The 7's are at indices 0 and 5 → distance = 5  
The minimum distance is 3.

Constraints:
-------------
1 <= n <= 10^3
1 <= a[i] <= 10^5
'''

def minimumDistances(a):
    # Store the last seen index of each number
    last_seen = {}
    min_distance = float('inf')

    for i, num in enumerate(a):
        if num in last_seen:
            distance = i - last_seen[num]
            min_distance = min(min_distance, distance)
        last_seen[num] = i

    # If no pairs found, return -1
    return min_distance if min_distance != float('inf') else -1

print(minimumDistances([7, 1, 3, 4, 1, 7]))  # Expected output: 3
print(minimumDistances([1, 2, 3, 4, 10]))    # Expected output: -1
print(minimumDistances([5, 5, 5, 5]))        # Expected output: 1
print(minimumDistances([2, 3, 2, 3, 2]))     # Expected output: 2
