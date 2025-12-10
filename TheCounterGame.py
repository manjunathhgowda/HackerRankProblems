'''
HackerRank Problem: Counter Game

Louise and Richard play a game starting with a counter n.
Rules:
- Louise moves first.
- On a player's turn:
    - If n is a power of 2, replace n with n / 2.
    - Otherwise, reduce n by the largest power of 2 less than n.
- The player who reduces n to 1 wins.

Observation / solution:
Each move either removes (clears) the highest set bit (when subtracting the largest power of two
less than n) or shifts the number right by one (when n is a power of two). Count how many moves
are required to reduce n to 1. If the total number of moves is odd, Louise (first player) wins;
if even, Richard wins.

Implement counterGame(n) which returns "Louise" or "Richard".
No main() — example calls shown below.
'''

def counterGame(n: int) -> str:
    # Special case: if n == 1, no moves possible, Louise loses
    if n == 1:
        return "Richard"

    moves = 0
    # Loop until n becomes 1
    while n > 1:
        # If n is a power of two (only one bit set)
        if (n & (n - 1)) == 0:
            n //= 2
        else:
            # subtract the largest power of two less than n
            highest_power = 1 << (n.bit_length() - 1)
            n -= highest_power
        moves += 1

    return "Louise" if (moves % 2 == 1) else "Richard"


# Example calls (no main, as you requested)
print(counterGame(6))   # Expected: Richard (sample from prompt)
print(counterGame(1))   # Expected: Richard (Louise can't move)
print(counterGame(2))   # Expected: Louise  (2 -> 1, 1 move)
print(counterGame(132)) # Some other test
