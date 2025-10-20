"""
Marc's Cakewalk

Problem:
Marc eats cupcakes, each with a certain calorie count.
After eating i cupcakes (0-indexed), for the (i+1)th cupcake with c calories,
he must walk 2^i * c miles to maintain his weight.

Goal:
Find the minimum total miles Marc must walk.

Logic:
To minimize total miles, eat the cupcakes with the highest calories first.
Why? Because earlier cupcakes have smaller exponents (2^i).

Steps:
1. Sort the calorie list in descending order.
2. Compute total = Σ (2^i * calorie[i])
3. Return the result as a long integer.
"""

def marcsCakewalk(calorie):
    # Sort in descending order to minimize walking distance
    calorie.sort(reverse=True)
    
    total_miles = 0
    for i in range(len(calorie)):
        total_miles += (2 ** i) * calorie[i]
    
    return total_miles


# Example tests (for understanding instead of __main__)
test_cases = [
    [1, 3, 2],     # Expected 11
    [7, 4, 9, 6],  # Expected 79
]

for c in test_cases:
    print(f"calorie = {c} → min miles = {marcsCakewalk(c)}")

"""
Expected Output:
calorie = [1, 3, 2] → min miles = 11
calorie = [7, 4, 9, 6] → min miles = 79
"""
