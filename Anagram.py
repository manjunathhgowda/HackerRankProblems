'''
Problem:
Two words are anagrams if their letters can be rearranged to form one another.

Given a string, split it into two contiguous substrings of equal length.
Determine the minimum number of characters to change to make the two substrings anagrams of one another.

If the string length is odd, return -1.

Example:
Input:
s = "aaabbb"
Output:
3

Explanation:
Split into "aaa" and "bbb".
We must change all 3 characters from the first half to 'b' to make them anagrams.
'''

def anagram(s):
    if len(s) % 2 != 0:
        return -1
    half = len(s) // 2
    s1 = s[:half]
    s2 = s[half:]
    # Convert s2 into a list to modify characters as we find matches
    s2_list = list(s2)
    for ch in s1:
        if ch in s2_list:
            s2_list.remove(ch)
    # The remaining unmatched characters in s2_list are the changes needed
    return len(s2_list)
# Example test cases
print(anagram("aaabbb"))     # Output: 3
print(anagram("ab"))         # Output: 1
print(anagram("abc"))        # Output: -1
print(anagram("mnop"))       # Output: 2
print(anagram("xyyx"))       # Output: 0
print(anagram("xaxbbbxx"))   # Output: 1
