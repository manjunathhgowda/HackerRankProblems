#!/bin/python3
'''
Picking Numbers

Problem:
Given an array of integers, find the length of the longest subarray 
where the absolute difference between any two elements is less than or equal to 1.

Example:
a = [4, 6, 5, 3, 3, 1]

The subarrays that meet the condition are:
[4, 5, 5] → difference = 1
[3, 3, 4] → difference = 1
The longest such subarray has 3 elements.

Function Description:
Complete the 'pickingNumbers' function below.

pickingNumbers has the following parameter(s):
    int a[n]: an array of integers

Returns:
    int: the length of the longest subarray that meets the criterion

Input Format:
The first line contains a single integer n, the size of the array a.
The second line contains n space-separated integers, each an a[i].

Constraints:
2 ≤ n ≤ 100
0 < a[i] < 100
The answer will be ≥ 2.

Sample Input 0:
6
4 6 5 3 3 1

Sample Output 0:
3

Explanation 0:
We choose the multiset [3, 3, 4]. Each pair has an absolute difference ≤ 1.
So we print 3.

Sample Input 1:
6
1 2 2 3 1 2

Sample Output 1:
5

Explanation 1:
We choose the multiset [1, 2, 2, 1, 2]. Each pair has difference ≤ 1.
So we print 5.
'''
def pickingNumbers(a):
    max_len = 0
    # Loop through each unique element
    for num in set(a):
        # Count numbers equal to num or num + 1
        count = a.count(num) + a.count(num + 1)
        if count > max_len:
            max_len = count
    return max_len
# Example test cases
print(pickingNumbers([4, 6, 5, 3, 3, 1]))  # Expected Output: 3
print(pickingNumbers([1, 2, 2, 3, 1, 2]))  # Expected Output: 5
