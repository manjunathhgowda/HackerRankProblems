'''
Game of Thrones - I
-------------------
Given a string s, determine if the characters of the string can be rearranged 
to form a palindrome. Return "YES" if possible, otherwise "NO".

Example:
Input: aaabbbb
Output: YES
Explanation: One possible palindrome is "bbaaabb".
'''

def gameOfThrones(s):
    # Count frequency of each character
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    
    # Count characters that appear odd number of times
    odd_count = 0
    for val in count.values():
        if val % 2 != 0:
            odd_count += 1

    # Palindrome possible if at most one char has an odd frequency
    if odd_count > 1:
        return "NO"
    else:
        return "YES"


# Example usage
print(gameOfThrones("aaabbbb"))       # YES
print(gameOfThrones("cdefghmnopqrstuvw"))  # NO
print(gameOfThrones("cdcdcdcdeeeef")) # YES
