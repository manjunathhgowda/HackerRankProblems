"""
CamelCase

There is a sequence of words in CamelCase as a string `s`, having the following properties:
- It is a concatenation of one or more words consisting of English letters.
- All letters in the first word are lowercase.
- Each subsequent word starts with an uppercase letter, followed by lowercase letters.

Task:
-----
Given `s`, determine the number of words in it.

Function Description:
---------------------
camelcase(s)
- s: string to analyze
Returns:
- int: number of words in the CamelCase string

Example:
--------
Input:
saveChangesInTheEditor

Output:
5

Explanation:
Words are: save, Changes, In, The, Editor
"""

def camelcase(s):
    count = 1
    for ch in s:
        if ch.isupper():
            count += 1
    return count
examples = [
    "saveChangesInTheEditor",  # Expected output: 5
    "oneTwoThree",             # Expected output: 3
    "hello",                   # Expected output: 1
    "thisIsCamelCaseTest",     # Expected output: 5
]
for s in examples:
    print(camelcase(s))
