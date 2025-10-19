"""
Electronics Shop

A person wants to buy **one keyboard** and **one USB drive** with a given budget.
Given lists of keyboard and USB drive prices, determine the **maximum money they can spend**.
Return -1 if it's impossible to buy both items.

Function:
----------
getMoneySpent(keyboards, drives, b)
- keyboards: list of integers, keyboard prices
- drives: list of integers, USB drive prices
- b: integer, budget
Returns:
- int: maximum spent, or -1 if no combination is affordable

Example:
--------
Input:
b = 10
keyboards = [3, 1]
drives = [5, 2, 8]

Output:
9
Explanation:
Buy keyboard 1 (price 1) and USB drive 8 → total = 9 (max possible ≤ budget)
"""

def getMoneySpent(keyboards, drives, b):
    max_spent = -1  # start with -1 for impossible case
    for k in keyboards:
        for d in drives:
            total = k + d
            if total <= b and total > max_spent:
                max_spent = total
    return max_spent
examples = [
    ([3, 1], [5, 2, 8], 10),  # Expected output: 9
    ([4], [5], 5),             # Expected output: -1
    ([4, 5], [2, 8], 8),       # Expected output: 8
]

for keyboards, drives, budget in examples:
    print(getMoneySpent(keyboards, drives, budget))
