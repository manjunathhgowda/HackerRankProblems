#!/bin/python3
'''
Repeated String

Problem:
There is a string, s, of lowercase English letters that is repeated infinitely many times. 
Given an integer n, find and print the number of letter 'a's in the first n letters 
of the infinite string.

Example:
s = "aba"
n = 10

The substring we consider is "abaabaabaa", the first 10 characters of the infinite string.
There are 7 occurrences of 'a' in this substring.

Function Description:
Complete the 'repeatedString' function below.

repeatedString has the following parameters:
    string s: a string to repeat
    int n: the number of characters to consider

Returns:
    int: the frequency of 'a' in the substring

Input Format:
The first line contains a single string, s.
The second line contains an integer, n.

Constraints:
1 ≤ |s| ≤ 100
1 ≤ n ≤ 10^12
For 25% of the test cases, n ≤ 10^6

Sample Input 0:
aba
10

Sample Output 0:
7

Explanation 0:
The first 10 letters of the infinite string are "abaabaabaa".
There are 7 'a's in the substring.

Sample Input 1:
a
1000000000000

Sample Output 1:
1000000000000

Explanation 1:
All of the first n letters are 'a', so the answer is 1000000000000.
'''


def repeatedString(s, n):
    # Count 'a's in one full instance of s
    count_a_in_s = s.count('a')
    
    # Find how many full times s fits in n characters
    full_repeats = n // len(s)
    
    # Find remaining characters
    remainder = n % len(s)
    
    # Count 'a's in the partial substring
    count_a_in_remainder = s[:remainder].count('a')
    
    # Total 'a's = (a's in full strings) + (a's in remainder)
    total_a = (count_a_in_s * full_repeats) + count_a_in_remainder
    return total_a
# Example test cases
print(repeatedString("aba", 10))           # Expected output: 7
print(repeatedString("a", 1000000000000))  # Expected output: 1000000000000
