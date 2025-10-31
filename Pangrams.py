#!/bin/python3

# HackerRank Problem: Pangrams
# A pangram is a string that contains every letter of the English alphabet at least once.
# Return "pangram" if it does, otherwise "not pangram".

def pangrams(s):
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in s.lower():
            return "not pangram"
    return "pangram"

# Example test cases (instead of using main)
examples = [
    "We promptly judged antique ivory buckles for the next prize",
    "We promptly judged antique ivory buckles for the prize"
]

for s in examples:
    print(pangrams(s))
