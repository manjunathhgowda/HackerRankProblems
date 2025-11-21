'''
HackerRank – Permuting Two Arrays

There are two n-element integer arrays, A and B. You must permute them
into A' and B' such that the condition below holds for all i:

    A'[i] + B'[i] >= k

If such a permutation exists, return "YES", otherwise return "NO".

Function Description
--------------------
Complete the function twoArrays(k, A, B).

Parameters:
    k : integer – the required minimum sum
    A : list[int] – first array
    B : list[int] – second array

Returns:
    string – "YES" or "NO"

Logic:
Sort A ascending.
Sort B descending.
If for every index i, A[i] + B[i] >= k → return "YES".
Otherwise → return "NO".

Example:
Input:
A = [2, 1, 3]
B = [7, 8, 9]
k = 10

Sorted:
A = [1, 2, 3]
B = [9, 8, 7]

Pairs:
1+9 = 10
2+8 = 10
3+7 = 10  → all >= 10 → YES
'''
def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)

    for a, b in zip(A, B):
        if a + b < k:
            return "NO"
    return "YES"


# ----- Example Calls (instead of main) -----

print(twoArrays(10, [2, 1, 3], [7, 8, 9]))
# Expected: YES

print(twoArrays(5, [1, 2, 2, 1], [3, 3, 3, 4]))
# Expected: NO
