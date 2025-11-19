'''
HackerRank - Sherlock and Array

Watson gives Sherlock an array of integers. Find if there exists an element
such that the sum of elements to its left equals the sum of elements to its right.

Return:
YES  -> if such an index exists
NO   -> otherwise

Logic:
1. Compute total sum of array.
2. Traverse array keeping a running left_sum.
3. For each element arr[i], right_sum = total_sum - left_sum - arr[i]
4. If left_sum == right_sum → return YES
5. If loop ends → return NO
'''

def balancedSums(arr):
    total = sum(arr)
    left_sum = 0
    
    for x in arr:
        if left_sum == total - left_sum - x:
            return "YES"
        left_sum += x

    return "NO"


# -------- Example calls (no main) --------

print(balancedSums([1, 2, 3]))        # Output: NO
print(balancedSums([1, 2, 3, 3]))     # Output: YES
print(balancedSums([1, 1, 4, 1, 1]))  # Output: YES
print(balancedSums([2, 0, 0, 0]))     # Output: YES
print(balancedSums([0, 0, 2, 0]))     # Output: YES
