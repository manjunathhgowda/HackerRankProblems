'''
Problem: XOR Strings

Given two binary strings consisting of digits 0 and 1 only,
find the XOR of the two strings.

For each bit position:
- If both bits are the same → result bit = 0
- If bits differ → result bit = 1

Example:
Input:
10101
00101

Output:
10000

Explanation:
1 XOR 0 = 1
0 XOR 0 = 0
1 XOR 1 = 0
0 XOR 0 = 0
1 XOR 1 = 0
Hence, result = 10000
'''

def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0'
        else:
            res += '1'
    return res


# Example test (instead of main/input)
s = "10101"
t = "00101"
print(strings_xor(s, t))  # Expected Output: 10000
