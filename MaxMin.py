'''
HackerRank Problem: Max Min

You are given an array of integers `arr` and an integer `k`.
Pick any `k` elements from `arr` to form a subarray `sub`.
The unfairness of `sub` is defined as:

    unfairness(sub) = max(sub) - min(sub)

Return the minimum possible unfairness achievable by choosing any `k` elements.

Approach (standard):
- Sort `arr`.
- Any optimal choice will be `k` consecutive elements in the sorted array.
- Slide a window of length `k` and compute arr[i+k-1] - arr[i], take the minimum.

Implement `maxMin(k, arr)` that returns the minimal unfairness.
No top-level `main()`; example calls are provided at the bottom.
'''

from typing import List

def maxMin(k: int, arr: List[int]) -> int:
    # Edge cases
    n = len(arr)
    if k <= 0 or n == 0 or k > n:
        return 0

    arr_sorted = sorted(arr)
    min_unfair = float('inf')

    # Slide window of size k
    for i in range(0, n - k + 1):
        unfair = arr_sorted[i + k - 1] - arr_sorted[i]
        if unfair < min_unfair:
            min_unfair = unfair

    return min_unfair


# Example calls (no main)
# Sample Input 0:
# n=7, k=3, arr = [10,100,300,200,1000,20,30]
print(maxMin(3, [10,100,300,200,1000,20,30]))  # Expected output: 20

# Sample Input 1:
# n=10, k=4, arr = [1,2,3,4,10,20,30,40,100,200]
print(maxMin(4, [1,2,3,4,10,20,30,40,100,200]))  # Expected output: 3

# Sample Input 2:
# n=5, k=2, arr = [1,2,1,2,1]
print(maxMin(2, [1,2,1,2,1]))  # Expected output: 0
