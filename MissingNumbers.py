'''
HackerRank – Missing Numbers

You are given two arrays:
- arr  = array with some numbers missing
- brr = original array (complete list)

A number is "missing" if its frequency in brr
is higher than its frequency in arr.

Rules:
• Return missing numbers in ascending order.
• Each missing number should appear only once.
• Frequency matters.

Example:
arr = [203,204,205,206,207,208,203,204,205,206]
brr = [203,204,204,205,206,207,205,208,203,206,205,206,204]

Missing numbers = [204, 205, 206]
'''

def missingNumbers(arr, brr):
    from collections import Counter

    countA = Counter(arr)
    countB = Counter(brr)

    missing = []

    for num in countB:
        if countB[num] > countA[num]:
            missing.append(num)

    return sorted(missing)



# ----- Example calls -----

print(missingNumbers(
    [203,204,205,206,207,208,203,204,205,206],
    [203,204,204,205,206,207,205,208,203,206,205,206,204]
))
# Expected Output: [204, 205, 206]

print(missingNumbers(
    [7,2,5,3,5,3],
    [7,2,5,4,6,3,5,3]
))
# Expected Output: [4, 6]
