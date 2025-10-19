"""
Tower Breakers

Two players are playing a game of Tower Breakers! Player 1 always moves first,
and both players always play optimally.

Rules:
- Initially there are n towers.
- Each tower is of height m.
- Players alternate turns.
- In a turn, a player chooses a tower of height h and reduces its height to h' such that
  1 <= h' < h and h % h' == 0 (h' evenly divides h).
- If a player cannot make a move, they lose.

Given n and m, determine which player wins:
Return 1 if Player 1 (the first player) wins, otherwise return 2.

Example:
Input:
2 2
1 4

Output:
2
1
"""

def towerBreakers(n, m):
    """
    Return 1 if Player 1 wins, otherwise 2.
    Rules-derived logic:
      - If m == 1: no moves possible, Player 2 wins.
      - If n is even: Player 2 can mirror Player 1's moves, so Player 2 wins.
      - Otherwise (n odd and m > 1): Player 1 wins.
    """
    if m == 1 or n % 2 == 0:
        return 2
    return 1

# Direct example calls (no __main__, no file I/O) — HackerRank sample cases:
examples = [
    (2, 2),  # expected output 2
    (1, 4)   # expected output 1
]

for n, m in examples:
    print(towerBreakers(n, m))
