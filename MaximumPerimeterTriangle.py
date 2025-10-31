"""
Maximum Perimeter Triangle

You are given an array of stick lengths. You must pick 3 of them to form a non-degenerate triangle
with the **maximum possible perimeter**.

Rules:
1. For a valid (non-degenerate) triangle: a + b > c  (where sides are sorted a ≤ b ≤ c)
2. If multiple triangles have the same perimeter:
   - Choose the one with the longest maximum side.
   - If still tied, choose the one with the longest minimum side.
3. If no triangle can be formed, return [-1].

Function:
----------
maximumPerimeterTriangle(sticks)

Input:
------
- sticks: list of integers representing stick lengths

Output:
-------
- list of 3 integers (triangle sides in non-decreasing order)
  OR [-1] if no valid triangle can be formed

Example:
--------
sticks = [1, 1, 1, 3, 3]  → Output: [1, 3, 3]
sticks = [1, 2, 3]        → Output: [-1]
"""

def maximumPerimeterTriangle(sticks):
    # Sort sticks in ascending order for triangle rule checking
    sticks.sort()

    # Start from largest side (max perimeter preference)
    for i in range(len(sticks) - 1, 1, -1):
        a = sticks[i - 2]
        b = sticks[i - 1]
        c = sticks[i]

        # Check non-degenerate triangle condition
        if a + b > c:
            return [a, b, c]

    # If no valid triangle found
    return [-1]


# Direct example test cases (no __main__, no file I/O)
examples = [
    [1, 1, 1, 3, 3],  # Expected output: [1, 3, 3]
    [1, 2, 3],        # Expected output: [-1]
    [1, 1, 1, 2, 3, 5],  # Expected output: [1, 1, 1]
    [2, 3, 4, 5, 10]     # Expected output: [3, 4, 5]
]

for sticks in examples:
    print(f"sticks = {sticks} → {maximumPerimeterTriangle(sticks)}")
