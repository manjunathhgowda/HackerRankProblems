'''
HackerRank Problem: Sansa and XOR

Sansa has an array. She wants to compute the XOR of all contiguous subarrays,
then XOR all those results together.

Brute force is slow. But mathematically:

Each element arr[i] appears in many subarrays.
Count how many times arr[i] contributes to the final XOR.

Index: 0-based
Total appearances = (i + 1) * (n - i)

If an element appears an ODD number of times, it contributes to final XOR.
If it appears EVEN times, it cancels out.

Result rule:
- If n is EVEN → answer = 0
- If n is ODD  → XOR of all elements at even indices (0,2,4,...)

Function:
Return the XOR result for the array.
'''

def sansaXor(arr):
    n = len(arr)

    # If length is even → result always 0
    if n % 2 == 0:
        return 0

    # If length is odd → XOR elements at even indices
    result = 0
    for i in range(0, n, 2):
        result ^= arr[i]

    return result


# Example calls (as requested, no main)
print(sansaXor([1, 2, 3]))         # 2
print(sansaXor([4, 5, 7, 5]))      # 0
print(sansaXor([98, 74, 12]))      # 110
print(sansaXor([50, 13, 2]))       # 48
