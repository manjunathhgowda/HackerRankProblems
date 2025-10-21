"""
Grid Challenge

Problem:
---------
Given a square grid of lowercase letters, rearrange each row alphabetically.
Then, check if the columns are also sorted top-to-bottom.
Return "YES" if all columns are sorted, otherwise "NO".

Example:
---------
grid = [
    "ebacd",
    "fghij",
    "olmkn",
    "trpqs",
    "xywuv"
]

After sorting rows:
[
    "abcde",
    "fghij",
    "klmno",
    "pqrst",
    "uvwxy"
]
→ Columns are sorted → Output: YES
"""

def gridChallenge(grid):
    sorted_grid = [''.join(sorted(row)) for row in grid]
    for col in range(len(sorted_grid[0])):
        for row in range(len(sorted_grid) - 1):
            if sorted_grid[row][col] > sorted_grid[row + 1][col]:
                return "NO"
    return "YES"

example1 = [
    "ebacd",
    "fghij",
    "olmkn",
    "trpqs",
    "xywuv"
]

example2 = [
    "mpxz",
    "abcd",
    "wlmf"
]

print("Example 1 Output:", gridChallenge(example1))  # Expected: YES
print("Example 2 Output:", gridChallenge(example2))  # Expected: NO



