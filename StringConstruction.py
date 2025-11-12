'''
Problem: String Construction
----------------------------

Amanda has a string of lowercase letters that she wants to copy to a new string. 
She can perform the following operations with given costs (any number of times):

1️⃣ Append a character to the end of string p at a cost of 1 dollar.  
2️⃣ Choose any substring of p and append it to the end of p at **no cost**.

Task:
-----
Given a string s, find and print the minimum cost of copying s.

Function Description:
---------------------
Complete the function stringConstruction in the editor below.
The function should return an INTEGER — the minimum cost to build string s.

Input Format:
-------------
The first line contains an integer q — number of test cases.
Each of the next q lines contains one string s.

Constraints:
------------
1 <= q <= 10
1 <= |s| <= 10^5
s contains only lowercase English letters (a-z)

Output Format:
--------------
For each query, print the minimum cost of constructing the string s.

Explanation:
------------
To build a string, you pay only for each *unique character* in s.
Because once you’ve added a character, you can reuse it via substring copying.

Example:
--------
Input:
2
abcd
abab

Output:
4
2

Explanation:
- For "abcd": All 4 characters are unique, so cost = 4.
- For "abab": Only 'a' and 'b' are unique, so cost = 2.
'''

def stringConstruction(s):
    return len(set(s))
examples = ["abcd", "abab"]
for s in examples:
    print(stringConstruction(s))
