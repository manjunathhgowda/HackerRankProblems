'''
HackerRank Problem: Two Strings

Given two strings, determine if they share a common substring.
A substring may be as small as one character.

Example:
---------
Input:
    s1 = "hello"
    s2 = "world"
Output:
    "YES"

Explanation:
    The strings share the common substring "o".

If there is no common substring, return "NO".

Function Description:
---------------------
Complete the function 'twoStrings' below.

twoStrings has the following parameter(s):
    string s1: a string
    string s2: another string

Returns:
    string: either "YES" or "NO"

Constraints:
    s1 and s2 consist of lowercase English letters ('a'–'z').

Sample Input:
    2
    hello
    world
    hi
    world

Sample Output:
    YES
    NO

Explanation:
    Test case 1: "hello" and "world" share "o" → YES
    Test case 2: "hi" and "world" share nothing → NO
'''

def twoStrings(s1, s2):
    # Convert both strings to sets of unique characters
    set1 = set(s1)
    set2 = set(s2)
    
    # If there is any common character, return YES
    if set1 & set2:
        return "YES"
    else:
        return "NO"


# Example usage (no __main__ block)
print(twoStrings("hello", "world"))  # Expected Output: YES
print(twoStrings("hi", "world"))     # Expected Output: NO
