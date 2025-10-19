"""
Jumping on the Clouds: Revisited

Problem:
A character jumps through circular clouds with step size `k`.
Each jump costs 1 energy unit.
If they land on a thundercloud (value = 1), they lose 2 more energy units.

We must find the remaining energy after the character returns to the starting cloud.

Example:
c = [0, 0, 1, 0, 0, 1, 1, 0], k = 2
Output: 92
Explanation:
Start energy = 100
Path: 0 → 2 → 4 → 6 → 0
Energy calculation:
- Jump 1: from 0 → 2 (thundercloud) → -3 (total 97)
- Jump 2: from 2 → 4 (cumulus) → -1 (total 96)
- Jump 3: from 4 → 6 (thundercloud) → -3 (total 93)
- Jump 4: from 6 → 0 (cumulus) → -1 (total 92)
"""

def jumpingOnClouds(c, k):
    energy = 100        # Start energy
    n = len(c)          # Number of clouds
    position = 0        # Starting position

    # Loop until we come back to start
    while True:
        # Move k steps forward (circular using modulo)
        position = (position + k) % n
        
        # Each jump costs 1 energy + 2 if thundercloud
        energy -= 1 + 2 * c[position]

        # Stop when we land back at the starting point
        if position == 0:
            break

    return energy

print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0], 2))   # Expected output: 92
print(jumpingOnClouds([0, 0, 0, 0, 1, 0], 3))         # Expected output: 94
