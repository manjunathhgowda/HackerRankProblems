'''
Problem: Palindrome Index

Given a string of lowercase letters in the range ascii[a-z], determine the index of a character 
that can be removed to make the string a palindrome. There may be more than one solution, 
but any will do. If the word is already a palindrome or there is no solution, return -1. 
Otherwise, return the index of a character to remove.

Example:
s = "aaab"
Either remove 'b' at index 3 or remove 'a' at index 0.
Removing 'b' makes "aaa", which is a palindrome. So output = 3.

Function Description:
Complete the function palindromeIndex below.

palindromeIndex has the following parameter(s):
    string s: a string to analyze

Returns:
    int: the index of the character to remove or -1

Input Format:
The first line contains an integer q, the number of queries.
Each of the next q lines contains a string s.

Constraints:
All characters are in the range ascii[a-z].

Sample Input:
3
aaab
baa
aaa

Sample Output:
3
0
-1
'''

def palindromeIndex(s):
    # Helper function to check palindrome
    def is_palindrome(x):
        return x == x[::-1]

    # If already palindrome
    if is_palindrome(s):
        return -1

    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            # Check by removing one side
            if is_palindrome(s[:i] + s[i+1:]):
                return i
            elif is_palindrome(s[:j] + s[j+1:]):
                return j
        i += 1
        j -= 1
    return -1


# Example usage (instead of main)
examples = ["aaab", "baa", "aaa", "abca", "abcdba"]
for s in examples:
    print(f"{s} → index to remove = {palindromeIndex(s)}")
