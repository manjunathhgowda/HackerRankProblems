'''
Lonely Integer

Given an array of integers, where all elements but one occur twice, find the unique element.

Example:
a = [1, 1, 2]
→ The unique element is 2.

Function Description:
Complete the lonelyinteger function below.

lonelyinteger has the following parameter(s):
    int a[n]: an array of integers

Returns:
    int: the element that occurs only once

Input Format:
The first line contains a single integer, n, the number of integers in the array.
The second line contains n space-separated integers that describe the values in a.

Constraints:
- It is guaranteed that n is an odd number and there is one unique element.
- 0 ≤ a[i] < 100, for all i.

Sample Input 0:
1
1
Sample Output 0:
1

Sample Input 1:
3
1 1 2
Sample Output 1:
2

Sample Input 2:
5
0 0 1 2 1
Sample Output 2:
2
'''

def lonelyinteger(a):
    freq = {}
    for i in a:
        freq[i] = freq.get(i, 0) + 1
    for k in freq:
        if freq[k] == 1:
            return k
    # Find and return the number that appears once
    for key, value in freq.items():
        if value == 1:
            return key
        
#shorter method using count()
# def lonelyinteger(a):
#     for i in a:
#         if a.count(i) == 1:
#             return i

print(lonelyinteger([1]))           # Output: 1
print(lonelyinteger([1, 1, 2]))     # Output: 2
print(lonelyinteger([0, 0, 1, 2, 1]))  # Output: 2
