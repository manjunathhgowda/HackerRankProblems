#!/bin/python3

"""
The Love-Letter Mystery

You are given a lowercase string `s`.
You can reduce the value of letters (e.g., 'd' → 'c') to make the string a palindrome.
Each such reduction counts as 1 operation.
Find the minimum number of operations needed to make `s` a palindrome.

Example:
    s = "abc" → "abb" → "aba" → 2 operations
"""

def theLoveLetterMystery(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    operations = 0
    left = 0
    right = len(s) - 1

    while left < right:
        # find index positions of each letter (0–25)
        left_index = alphabet.index(s[left])
        right_index = alphabet.index(s[right])

        # difference in their positions gives number of operations
        operations += abs(left_index - right_index)

        left += 1
        right -= 1

    return operations


# Example test cases (direct function calls, no input reading)
examples = ["abc", "abcba", "abcd", "cba"]

for s in examples:
    print(f"{s} → {theLoveLetterMystery(s)}")
