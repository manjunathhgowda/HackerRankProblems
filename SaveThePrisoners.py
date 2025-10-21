# """
# Save the Prisoner!

# Problem:
# ----------
# There are n prisoners sitting in a circle, numbered 1 to n.
# The jailer starts distributing m sweets beginning with seat number s.
# Each prisoner gets one sweet sequentially.
# The last sweet (the bad one) is given to one prisoner — find their seat number.

# Function:
# ----------
# saveThePrisoner(n, m, s)

# Parameters:
# n → number of prisoners
# m → number of sweets
# s → chair number to start passing sweets from

# Returns:
# Integer → the chair number of the prisoner who gets the bad sweet.
# """

# def saveThePrisoner(n, m, s):
#     result = (s + m - 1) % n
#     if result != 0:
#         return result     
#     else :
#         return n

# examples = [
#     (5, 2, 1),  # Expected: 2
#     (5, 2, 2),  # Expected: 3
#     (7, 19, 2), # Expected: 6
#     (3, 7, 3)   # Expected: 3
# ]

# for n, m, s in examples:
#     print(f"n={n}, m={m}, s={s} → {saveThePrisoner(n, m, s)}")

# """
# Expected Output:
# n=5, m=2, s=1 → 2
# n=5, m=2, s=2 → 3
# n=7, m=19, s=2 → 6
# n=3, m=7, s=3 → 3
# """
s="xyz"