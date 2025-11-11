'''
Problem: Lisa's Workbook

Lisa has a workbook with n chapters and k problems per page.
Each chapter i has arr[i] problems numbered from 1 to arr[i].
A problem is "special" if its problem number is the same as the page number it appears on.

Given n, k, and arr, return the total number of special problems.

Example:
n = 5, k = 3, arr = [4, 2, 6, 1, 10]
Output: 4
Explanation: There are 4 special problems in total.
'''

def workbook(n, k, arr):
    page = 1       # Current page number
    special = 0    # Count of special problems
    
    for problems in arr:
        for problem in range(1, problems + 1):
            if problem == page:  # Special problem
                special += 1
            if problem % k == 0 or problem == problems:
                page += 1        # Move to next page after k problems or end of chapter
    return special


# Example usage (like HackerRank custom input)
n = 5
k = 3
arr = [4, 2, 6, 1, 10]
print(workbook(n, k, arr))  # Output: 4
