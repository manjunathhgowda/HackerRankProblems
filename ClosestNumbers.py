'''
HackerRank - Closest Numbers

Given an array of unique integers, find all pairs of elements 
with the smallest absolute difference between them.

Steps:
1. Sort the array.
2. Compute differences of consecutive elements.
3. Track the smallest difference.
4. Collect all pairs that match this difference.
5. Return them in a single flat list.
'''

def closestNumbers(arr):
    arr.sort()
    result = []
    min_diff = float('inf')

    # Find minimum absolute difference
    for i in range(len(arr) - 1):
        diff = arr[i+1] - arr[i]
        if diff < min_diff:
            min_diff = diff
            result = [arr[i], arr[i+1]]
        elif diff == min_diff:
            result.extend([arr[i], arr[i+1]])

    return result


# ------- Example calls instead of main() --------

print(closestNumbers([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]))
# Output: [-20, 30]

print(closestNumbers([-20, -3916237, -357920, -3620601, 7374819,
                      -7330761, 30, 6246457, -6461594, 266854, -520, -470]))
# Output: [-520, -470, -20, 30]

print(closestNumbers([5, 4, 3, 2]))
# Output: [2, 3, 3, 4, 4, 5]
