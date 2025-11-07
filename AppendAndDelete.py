
'''
Append and Delete

You have two strings of lowercase English letters. You can perform two types of operations on the first string:
1. Append a lowercase English letter to the end of the string.
2. Delete the last character of the string. Performing this operation on an empty string results in an empty string.

Given an integer k and two strings s and t, determine whether or not you can convert s to t by performing exactly k operations.
If it's possible, print "Yes". Otherwise, print "No".

Example:
----------
s = "hackerhappy"
t = "hackerrank"
k = 9
Output: Yes

Explanation:
We delete "appy" (4 operations) and then append "rank" (5 operations), total = 9. So, print Yes.

Function Description:
----------------------
Complete the appendAndDelete function below.
- appendAndDelete has the following parameters:
    string s: the initial string
    string t: the desired string
    int k: the number of operations
Returns:
    string: either "Yes" or "No"

Sample Input 1:
aba
aba
7
Output: Yes

Sample Input 2:
ashley
ash
2
Output: No
'''

def appendAndDelete(s, t, k):
    # Find the common prefix length
    common_length = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            common_length += 1
        else:
            break

    # Calculate the minimum number of operations needed
    total_ops = (len(s) - common_length) + (len(t) - common_length)

    # Check if we can perform exactly k operations
    if k >= len(s) + len(t):
        return "Yes"
    elif total_ops <= k and (k - total_ops) % 2 == 0:
        return "Yes"
    else:
        return "No"


# Example test cases (instead of using __main__)
print(appendAndDelete("hackerhappy", "hackerrank", 9))   # Expected: Yes
print(appendAndDelete("aba", "aba", 7))                  # Expected: Yes
print(appendAndDelete("ashley", "ash", 2))               # Expected: No
