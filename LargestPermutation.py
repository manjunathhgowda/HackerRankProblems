'''
HackerRank - Largest Permutation

You are given an array containing all integers from 1 to n in random order.
You may perform at most k swaps.

Goal:
Return the lexicographically largest permutation possible using ≤ k swaps.

Logic:
- For each index i, the ideal value we want is n - i (largest to smallest).
- If arr[i] is already correct, continue.
- Otherwise, swap arr[i] with the index where the correct value is located.
- Use a hashmap (value → index) for O(1) lookup.
- Decrease k after each swap. Stop when k reaches 0.
'''

def largestPermutation(k, arr):
    n = len(arr)
    # Map each value to its index
    pos = {value: idx for idx, value in enumerate(arr)}
    
    target = n  # The value we want at index 0, then n-1 at index 1, etc.
    
    for i in range(n):
        if k == 0:
            break
        
        # If this index already has the correct (largest possible) value
        if arr[i] == target:
            target -= 1
            continue
        
        # Index of where the desired value is currently located
        correct_idx = pos[target]
        
        # Swap arr[i] with arr[correct_idx]
        arr[i], arr[correct_idx] = arr[correct_idx], arr[i]
        
        # Update positions in hash map
        pos[arr[correct_idx]] = correct_idx
        pos[arr[i]] = i
        
        k -= 1
        target -= 1
    
    return arr


# Example calls (same as HackerRank)
print(largestPermutation(1, [4, 2, 3, 5, 1]))   # Output: [5, 2, 3, 4, 1]
print(largestPermutation(1, [2, 1, 3]))         # Output: [3, 1, 2]
print(largestPermutation(1, [2, 1]))            # Output: [2, 1]
