'''
HackerRank – Forming a Magic Square

We define a magic square to be a 3×3 matrix of distinct positive integers from 1 to 9,
where the sum of every row, column, and diagonal is equal to the same constant.

You are given a 3×3 matrix "s".
You can change any number 'a' into any number 'b' at a cost of |a - b|.

Your task:
Convert the given matrix into a magic square with minimal total cost.
Return this minimum cost.

Example:
s = [
    [5, 3, 4],
    [1, 5, 8],
    [6, 4, 2]
]

Output: 7
'''

def formingMagicSquare(s):
    # All possible 3x3 magic squares (there are only 8)
    magic_squares = [
        [8,1,6,3,5,7,4,9,2],
        [6,1,8,7,5,3,2,9,4],
        [4,9,2,3,5,7,8,1,6],
        [2,9,4,7,5,3,6,1,8],
        [8,3,4,1,5,9,6,7,2],
        [4,3,8,9,5,1,2,7,6],
        [6,7,2,1,5,9,8,3,4],
        [2,7,6,9,5,1,4,3,8],
    ]

    # Flatten input for easy comparison
    flat = [num for row in s for num in row]

    min_cost = float('inf')

    # Compare to each magic square
    for magic in magic_squares:
        cost = 0
        for a, b in zip(flat, magic):
            cost += abs(a - b)
        min_cost = min(min_cost, cost)

    return min_cost

example = [
    [5, 3, 4],
    [1, 5, 8],
    [6, 4, 2]
]

print(formingMagicSquare(example))   # Expected Output: 7
