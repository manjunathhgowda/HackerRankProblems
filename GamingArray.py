'''
HackerRank Problem: Gaming Array

Two players (Bob first, then Andy) play a game.
Rules:
- On each turn, a player removes the maximum element of the array
  and all elements to its right.
- Players alternate.
- Last player able to make a move wins.

Observation:
Each time we encounter a new maximum from the left, a move happens.
Count how many such maximums appear.
If the count is odd → Bob wins.
If even → Andy wins.

Implement gamingArray(arr)
Return "BOB" or "ANDY".
'''

def gamingArray(arr):
    moves = 0
    max_so_far = 0

    for num in arr:
        if num > max_so_far:
            max_so_far = num
            moves += 1   # New maximum → player makes a move

    return "BOB" if moves % 2 == 1 else "ANDY"


# Example calls (no main, as you requested)
print(gamingArray([5, 2, 6, 3, 4]))   # Expected ANDY
print(gamingArray([3, 1]))           # Expected BOB
print(gamingArray([1, 3, 5, 7, 9]))  # Expected BOB
print(gamingArray([7, 4, 6, 5, 9]))  # Expected ANDY
