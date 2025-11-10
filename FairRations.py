'''
Problem:
You are the benevolent ruler of Rankhacker Castle, and today you're distributing bread.
Your subjects are in a line, and some of them already have some loaves. 
You must distribute as few loaves as possible so that each person ends up with an even number of loaves.

Rules:
- Every time you give a loaf to someone, you must also give one to their neighbor (either front or behind).
- After distribution, everyone must have an even number of loaves.

If it’s impossible, print "NO".
Example:
Input:
B = [2, 3, 4, 5, 6]
Output:
'4'

Explanation:
Give a loaf to person 2 and 3 → [2, 4, 5, 5, 6]
Then give a loaf to person 3 and 4 → [2, 4, 6, 6, 6]
Total = 4 loaves distributed.
'''

def fairRations(B):
    loaves = 0
    for i in range(len(B) - 1):
        if B[i] % 2 != 0:       # If current person has odd loaves
            B[i] += 1           # Give one loaf to this person
            B[i + 1] += 1       # And one to the next person
            loaves += 2         # Count two loaves given
    if B[-1] % 2 != 0:          # If last person is still odd, it's impossible
        return "NO"
    return str(loaves)

# Example test
print(fairRations([2, 3, 4, 5, 6]))   # Output: 4
print(fairRations([1, 2]))            # Output: NO
