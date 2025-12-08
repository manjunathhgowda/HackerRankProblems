'''
HackerRank Problem: Flipping the Matrix

Sean can reverse any row or column of a 2n x 2n matrix any number of times.
Goal: maximize the sum of elements in the n x n upper-left quadrant.

Observation / solution:
For each cell (i, j) in the n x n upper-left quadrant, we can choose which value
among its four symmetric positions to bring into that quadrant:
  (i, j), (i, 2n-1-j), (2n-1-i, j), (2n-1-i, 2n-1-j)
So the optimal value for that position is the maximum of those four values.
Sum those maxima over i in [0..n-1] and j in [0..n-1].

Implement flippingMatrix(matrix) which accepts a 2n x 2n list of lists and
returns the maximal possible sum for the upper-left quadrant.
No main() — example calls shown below.
'''

def flippingMatrix(matrix):
    size = len(matrix)              # 2n
    n = size // 2
    total = 0
    for i in range(n):
        for j in range(n):
            # four symmetric candidates
            a = matrix[i][j]
            b = matrix[i][size - 1 - j]
            c = matrix[size - 1 - i][j]
            d = matrix[size - 1 - i][size - 1 - j]
            total += max(a, b, c, d)
    return total


# Example from the prompt
mat = [
    [112, 42, 83, 119],
    [56, 125, 56, 49],
    [15, 78, 101, 43],
    [62, 98, 114, 108]
]
print(flippingMatrix(mat))  # Expected output: 414

# Additional small tests
# 2x2 (n=1) example:
mat2 = [
    [1, 2],
    [3, 4]
]
# Best upper-left (1x1) is max(1,2,3,4)=4
print(flippingMatrix(mat2))  # Expected output: 4

# 4x4 with all equal values -> sum is n*n * that value
mat3 = [[5]*4 for _ in range(4)]
print(flippingMatrix(mat3))  # Expected output: 5 * 2 * 2 = 20
