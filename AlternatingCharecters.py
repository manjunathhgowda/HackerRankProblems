'''HackerRank Problem: Alternating Characters
Given a string consisting of 'A' and 'B' characters,
delete the minimum number of characters to make the string
have no matching adjacent characters.'''

def alternatingCharacters(s):
    count = 0
    prev = s[0]
    for i in range(1, len(s)):
        if prev == s[i]:
            count += 1
        prev = s[i]
    return count


# Example test cases (instead of main)
examples = [
    "AAAA",
    "BBBBB",
    "ABABABAB",
    "BABABA",
    "AAABBB"
]

# Expected output:
# 3
# 4
# 0
# 0
# 4

for s in examples:
    print(alternatingCharacters(s))
