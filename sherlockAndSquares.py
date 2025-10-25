'''
Circular Array Rotation

John Watson knows of an operation called a right circular rotation on an array of integers.
One rotation operation moves the last array element to the first position and shifts all remaining 
elements right by one. To test Sherlock's abilities, Watson provides an array of integers.
Sherlock must perform the rotation operation a number of times, then determine the value of the 
element at a given position.

Function Description:
----------------------
Complete the function `circularArrayRotation(a, k, queries)` below.

Parameters:
------------
int a[n]: the array to rotate
int k: the number of rotations
int queries[q]: the indices to report after rotation

Returns:
---------
int[q]: the values at the requested indices after rotation

Example:
---------
Input:
a = [1, 2, 3]
k = 2
queries = [0, 1, 2]

After 2 right rotations:
[2, 3, 1]

Output:
[2, 3, 1]

Explanation:
------------
After each rotation:
1st → [3, 1, 2]
2nd → [2, 3, 1]
Thus:
index 0 → 2
index 1 → 3
index 2 → 1

Constraints:
------------
1 <= n <= 10^5
1 <= a[i] <= 10^5
1 <= k <= 10^5
1 <= q <= 500
'''

def circularArrayRotation(a, k, queries):
    n = len(a)
    k = k % n
    rotated = a[-k:] + a[:-k]
    return [rotated[i] for i in queries]
# Example test cases (instead of HackerRank input)
print(circularArrayRotation([1, 2, 3], 2, [0, 1, 2]))   # Output: [2, 3, 1]
print(circularArrayRotation([1, 2, 3, 4, 5], 3, [1, 3])) # Output: [4, 1]
print(circularArrayRotation([7, 8, 9], 1, [0, 1, 2]))    # Output: [9, 7, 8]
