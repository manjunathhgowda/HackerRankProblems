'''
Question:
Given an array of integers, find the sum of its elements.

For example, if the array = [1, 2, 3], 
the sum is 1 + 2 + 3 = 6, so return 6.

Function Description:
Complete the 'simpleArraySum' function below.

Parameters:
    ar: an array of integers

Returns:
    The sum of the array elements as an integer.

Input Format:
    - The first line contains an integer, n, denoting the size of the array.
    - The second line contains n space-separated integers representing the array's elements.

Constraints:
    0 < n, ar[i] <= 1000

Sample Input:
6
1 2 3 4 10 11

Sample Output:
31

Explanation:
The sum of the array's elements is 1 + 2 + 3 + 4 + 10 + 11 = 31.
'''

def simpleArraySum(ar):
    return sum(ar)
print(simpleArraySum([1,2,3,4,10,11]))