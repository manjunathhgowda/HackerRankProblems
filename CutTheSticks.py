'''
Problem:Cut The Sticks
You are given a number of sticks of varying lengths. You will iteratively cut the sticks into smaller sticks,
discarding the shortest pieces until there are none left.

At each iteration:
- Find the length of the shortest stick.
- Cut that length from all longer sticks.
- Discard all sticks that become 0 length.
- Print how many sticks are left before each iteration.

Example:
Input:
arr = [5, 4, 4, 2, 2, 8]

Output:
[6, 4, 2, 1]

Explanation:
Iteration 1: shortest = 2 → [3, 2, 2, 0, 0, 6] → remove 0s → [3, 2, 2, 6]
Iteration 2: shortest = 2 → [1, 0, 0, 4] → remove 0s → [1, 4]
Iteration 3: shortest = 1 → [0, 3] → remove 0s → [3]
Iteration 4: shortest = 3 → [0] → remove 0s → []
Counts = [6, 4, 2, 1]
'''

def cutTheSticks(arr):
    result = []
    arr.sort()
    while arr:
        result.append(len(arr))
        smallest = arr[0]
        arr = [x - smallest for x in arr if x - smallest > 0]
    return result
# Example test case
print(cutTheSticks([5, 4, 4, 2, 2, 8]))   # Output: [6, 4, 2, 1]
print(cutTheSticks([1, 2, 3, 4, 3, 3, 2, 1]))  # Output: [8, 6, 4, 1]
