#!/bin/python3
'''
HackerRank Problem: Sum vs XOR

Given an integer n, find the number of values x such that:

    n + x = n ^ x

where ^ denotes the bitwise XOR operator.

Return the count of such x values.

Input Format

A single integer, n.
    
Constraints                                                    
0 ≤ n ≤ 10^15

Output Format
An integer representing the number of possible x values.

Sample Input 0
5

Sample Output 0
2

Explanation 0
For n = 5 (binary 101), the following x values satisfy:
    5 + 2 = 7 and 5 ^ 2 = 7
    5 + 0 = 5 and 5 ^ 0 = 5
Thus, result = 2.

Sample Input 1
10

Sample Output 1
4

Explanation 1
For n = 10 (binary 1010), the possible x values are 0, 1, 4, and 5.
Thus, result = 4.
'''

def sumXor(n):
    # For any bit position that is 0 in n, x can have 0 or 1 (2 possibilities)
    # For bit position that is 1 in n, x must be 0
    # Therefore, number of valid x = 2^(count of zero bits in n)
    
    # Edge case: if n == 0, then all bits are 0 ⇒ infinite pattern, but in this case answer = 1
    if n == 0:
        return 1
    
    # Count number of 0 bits in binary representation of n
    zero_bits = bin(n)[2:].count('0')
    
    # Return 2 raised to that count
    return 2 ** zero_bits


# Example test cases (direct call instead of __main__)
examples = [5, 10, 0]

for n in examples:
    print(f"n = {n} → {sumXor(n)}")
