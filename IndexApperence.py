'''
HackerRank - Intro to Tutorial Challenges

Given a sorted array (arr) and a value (V),
return the index of V in the array.
V appears exactly once.

Example:
Input:
V = 4
arr = [1, 4, 5, 7, 9, 12]

Output:
1
'''

def introTutorial(V, arr):
    for i in range(len(arr)):
        if arr[i] == V:
            return i

# Example call
print(introTutorial(4, [1, 4, 5, 7, 9, 12]))
