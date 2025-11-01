'''
Beautiful Triplets

Problem:
Given a sequence of integers `arr` and an integer `d`, 
a beautiful triplet is a set of three integers `(arr[i], arr[j], arr[k])`
such that:
    i < j < k
    arr[j] - arr[i] == d
    arr[k] - arr[j] == d

You must count the number of beautiful triplets in the sequence.

Example:
d = 3
arr = [1, 2, 4, 5, 7, 8, 10]

The beautiful triplets are:
(1, 4, 7)
(2, 5, 8)
(4, 7, 10)
Output: 3
'''


def beautifulTriplets(d, arr):
    count = 0
    n = len(arr)
    
    # Loop through each i, j, k combination
    for i in range(n):
        for j in range(i + 1, n):
            # Check first difference condition
            if arr[j] - arr[i] == d:
                for k in range(j + 1, n):
                    # Check second difference condition
                    if arr[k] - arr[j] == d:
                        count += 1
    return count


# Example test case
d = 3
arr = [1, 2, 4, 5, 7, 8, 10]

print(beautifulTriplets(d, arr))  # Expected Output: 3
