'''
HackerRank - Manasa and Stones

Given:
- n: number of non-zero stones
- a, b: two possible differences
Starting stone is 0.
Return all possible values of the last stone, sorted ascending.

Logic:
Last stone value = i*a + (n-1-i)*b   for i in 0..(n-1)
Collect all unique values.
'''

def stones(n, a, b):
    result = set()
    for i in range(n):
        value = i * a + (n - 1 - i) * b
        result.add(value)
    return sorted(result)


# Example calls (same as HackerRank)
print(stones(3, 1, 2))     # Output: [2, 3, 4]
print(stones(4, 10, 100))  # Output: [30, 120, 210, 300]
