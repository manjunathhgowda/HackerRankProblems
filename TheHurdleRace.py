#!/bin/python3
"""
The Hurdle Race

A video game character competes in a hurdle race. 
Hurdles are of varying heights, and the character can jump up to height `k` naturally. 
They can take doses of a magic potion — each dose increases their maximum jump height by 1 unit.

Task:
Determine the minimum number of doses required for the character to clear all hurdles.
If the character can already jump all hurdles, return 0.

Function Description
--------------------
hurdleRace(k, height):
- k: integer, natural jump height
- height: list of integers, each representing hurdle height
Return: integer — minimum number of doses required.

Example:
---------
Input:
5 4
1 6 3 5 2

Output:
2

Explanation:
Max hurdle height = 6
Natural jump = 4
Needs 6 - 4 = 2 doses.

Another Example:
----------------
Input:
5 7
2 5 4 5 2

Output:
0

Because the character can already jump all hurdles.
"""

def hurdleRace(k, height):
    # Find the tallest hurdle
    max_height = max(height)
    
    # If jump power is less than tallest hurdle, need extra doses
    if k < max_height:
        return max_height - k
    else:
        return 0

# ✅ Direct sample test cases (no file I/O)
examples = [
    (4, [1, 6, 3, 5, 2]),  # Expected output: 2
    (7, [2, 5, 4, 5, 2])   # Expected output: 0
]

for k, h in examples:
    print(hurdleRace(k, h))
