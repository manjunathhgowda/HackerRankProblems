"""
Separate the Numbers

A string is 'beautiful' if it can be split into a sequence of two or more consecutive positive integers,
such that:
    - Each number is exactly 1 greater than the previous.
    - No number has leading zeros.
    - The sequence follows the same order as in the string.

Example:
    "1234" → YES 1   (1,2,3,4)
    "91011" → YES 9  (9,10,11)
    "101103" → NO
"""

def separateNumbers(s):
    # If the string has only 1 character, it cannot be split → NO
    if len(s) == 1:
        print("NO")
        return

    # Try all possible lengths for the first number
    for i in range(1, len(s)//2 + 1):
        first = s[:i]              # Take the first number
        num = int(first)           # Convert it to integer
        formed = first             # String that we will build step-by-step

        # Keep adding consecutive numbers to the formed string
        while len(formed) < len(s):
            num += 1
            formed += str(num)

        # If the formed string matches the original, it's beautiful
        if formed == s:
            print("YES", first)
            return

    # If no sequence matched, print NO
    print("NO")


# Example test cases (direct calls without __main__)
examples = [
    "1234",      # YES 1
    "91011",     # YES 9
    "99100",     # YES 99
    "101103",    # NO
    "010203",    # NO
    "13",        # NO
    "1",         # NO
    "99910001001",  # YES 999
    "7891011",      # YES 7
    "9899100",      # YES 98
    "999100010001"  # NO
]

for s in examples:
    print(f"Input: {s}")
    separateNumbers(s)
    print()
