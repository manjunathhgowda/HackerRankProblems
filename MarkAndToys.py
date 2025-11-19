'''
HackerRank - Mark and Toys

Given a list of toy prices and a budget k,
find the maximum number of toys Mark can buy.

Logic:
- Sort the prices (cheapest first).
- Keep buying toys while the total cost ≤ k.
- Stop when adding the next toy exceeds the budget.
'''

def maximumToys(prices, k):
    prices.sort()  # buy cheapest first
    count = 0
    total = 0

    for p in prices:
        if total + p <= k:
            total += p
            count += 1
        else:
            break

    return count


# Example calls (instead of main)
print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50))  
# Output: 4

print(maximumToys([20, 30, 50, 10, 5], 60))
# Output: 3 (5 + 10 + 20)

print(maximumToys([3, 7, 2, 9], 1))
# Output: 0
