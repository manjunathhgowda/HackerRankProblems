#!/bin/python3
'''
HackerRank Problem: Funny String

In this challenge, you will determine whether a string is funny or not.  
To determine whether a string is funny, create a copy of the string in reverse.  
Iterating through each string, compare the absolute difference in the ASCII values  
of the characters at positions 0 and 1, 1 and 2, and so on to the end.  

If the list of absolute differences is the same for both strings, the string is "Funny".  
Otherwise, it is "Not Funny".

Function Description  
--------------------
Complete the function `funnyString` below.

funnyString has the following parameter(s):  
    string s: a string to test  

Returns  
    string: either "Funny" or "Not Funny"

Input Format  
-------------
The first line contains an integer q, the number of queries.  
The next q lines each contain a string s.

Example Input  
--------------
2  
acxz  
bcxz  

Example Output  
---------------
Funny  
Not Funny  

Explanation  
-----------
Test Case 0:  
s = "acxz", reverse = "zxca"  
ASCII values: [97, 99, 120, 122] and [122, 120, 99, 97]  
Differences: [2, 21, 2] for both → "Funny"

Test Case 1:  
s = "bcxz", reverse = "zxcb"  
Differences: [1, 21, 2] and [2, 21, 1] → "Not Funny"
'''

def funnyString(s):
    # Reverse the string
    rev_s = s[::-1]
    
    # Create lists of ASCII values
    s_ascii = [ord(ch) for ch in s]
    rev_ascii = [ord(ch) for ch in rev_s]
    
    # Compute absolute differences between consecutive characters
    diff_s = [abs(s_ascii[i+1] - s_ascii[i]) for i in range(len(s_ascii)-1)]
    diff_rev = [abs(rev_ascii[i+1] - rev_ascii[i]) for i in range(len(rev_ascii)-1)]
    
    # Compare both difference lists
    if diff_s == diff_rev:
        return "Funny"
    else:
        return "Not Funny"


# Example test cases (direct function calls instead of __main__)
examples = ["acxz", "bcxz"]

for s in examples:
    print(f"{s} -> {funnyString(s)}")
