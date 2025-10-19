"""
Game of Stones

Problem:
Two players take turns removing 2, 3, or 5 stones.
The player who cannot make a move loses.
Determine who wins if both play optimally.

Logic:
This is a classic pattern problem.
If n % 7 == 0 or n % 7 == 1, then "Second" wins.
Otherwise, "First" wins.

Why?
→ Losing positions repeat every 7 (0 and 1 are losing).
→ For all other values, "First" can always force a win.
"""

def gameOfStones(n):
    # Return 'First' if first player wins, else 'Second'
    return "Second" if n % 7 == 0 or n % 7 == 1 else "First"

# Example test cases (instead of __main__)
test_cases = [1, 2, 3, 4, 5, 6, 7, 10]

for n in test_cases:
    print(f"n = {n} → {gameOfStones(n)}")

"""
Expected Output:
n = 1 → Second
n = 2 → First
n = 3 → First
n = 4 → First
n = 5 → First
n = 6 → First
n = 7 → Second
n = 10 → First
"""
