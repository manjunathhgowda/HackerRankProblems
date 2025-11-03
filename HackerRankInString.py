#!/bin/python3
'''
HackerRank in a String!

Problem:
We say that a string contains the word "hackerrank" if a subsequence of its characters spell 
the word "hackerrank". Remember that a subsequence maintains the order of characters 
selected from a sequence.

More formally, let i0, i1, i2, ..., i9 be the respective indices of 
h, a, c, k, e, r, r, a, n, k in string s. 
If i0 < i1 < i2 < ... < i9 is true, then s contains "hackerrank".

For each query, print "YES" on a new line if the string contains "hackerrank" 
as a subsequence, otherwise print "NO".

Example:
Input:
2
hereiamstackerrank
hackerworld

Output:
YES
NO

Explanation:
The first string contains all letters of "hackerrank" in correct order.
The second string does not contain all letters in order.

Function Description:
Complete the 'hackerrankInString' function below.

hackerrankInString has the following parameter(s):
    string s: the string to search

Returns:
    string: "YES" or "NO"

Constraints:
1 ≤ |s| ≤ 10000
1 ≤ q ≤ 10

Sample Input 1:
2
hhaacckkekraraannk
rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt

Sample Output 1:
YES
NO
'''

def hackerrankInString(s):
    # target subsequence to find
    target = "hackerrank"
    j = 0  # pointer for target
    
    # Loop through given string
    for ch in s:
        # if current character matches current target character
        if ch == target[j]:
            j += 1  # move to next letter in 'hackerrank'
        # stop if all letters matched
        if j == len(target):
            return "YES"
    # if loop ends and not all matched
    return "NO"


# Example test cases
print(hackerrankInString("hereiamstackerrank"))   # Expected: YES
print(hackerrankInString("hackerworld"))          # Expected: NO
print(hackerrankInString("hhaacckkekraraannk"))   # Expected: YES
print(hackerrankInString("rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt"))  # Expected: NO
