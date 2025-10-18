
'''
Question:
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

Example:
Matrix:
1 2 3
4 5 6
9 8 9

The left-to-right (primary) diagonal = 1 + 5 + 9 = 15  
The right-to-left (secondary) diagonal = 3 + 5 + 9 = 17  
Their absolute difference = |15 - 17| = 2

Sample Input:
11 2 4
4 5 6
10 8 -12

Sample Output:
15

Explanation:
Primary diagonal = 11 + 5 + (-12) = 4  
Secondary diagonal = 4 + 5 + 10 = 19  
Absolute difference = |4 - 19| = 15
'''

def diagonalDifference(arr):
    n = len(arr)
    primary_sum = 0
    secondary_sum = 0
    for i in range(n):
        primary_sum += arr[i][i]           # Left-to-right diagonal
        secondary_sum += arr[i][n - i - 1] # Right-to-left diagonal
    return abs(primary_sum - secondary_sum)

matrix=[
    [11,2,4],
    [4,5,6],
    [10,8,-12]
]
print(diagonalDifference(matrix))
