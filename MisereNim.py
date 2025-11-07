'''
Misère Nim

Two people are playing a game of Misère Nim.

Rules:
--------
- The game starts with n piles of stones.
- Each pile i has s[i] stones.
- Players alternate turns.
- On each turn, a player must remove one or more stones from a single pile.
- The player who removes the last stone **loses** the game.

Task:
------
Given the number of stones in each pile, determine whether the first or second player wins 
assuming both play optimally.

Function Description:
----------------------
Complete the function misereNim below.

misereNim has the following parameter:
- int s[n]: number of stones in each pile

Returns:
- string: "First" if the first player will win, otherwise "Second".

Input Format:
--------------
The first line contains an integer t — number of test cases.
Each test case consists of:
1. An integer n — number of piles.
2. n space-separated integers s[i] — number of stones in each pile.

Constraints:
-------------
1 ≤ t ≤ 100
1 ≤ n ≤ 100
1 ≤ s[i] ≤ 10^9

Sample Input:
--------------
2
2
1 1
3
2 1 3

Sample Output:
--------------
First
Second

Explanation:
-------------
Test case 1:
- Two piles of one stone each. First player removes one stone from a pile.
- Second player has no choice but to take the last stone and loses.

Test case 2:
- No matter what move the first player makes, the second player wins with optimal play.
'''

def misereNim(s):
    # Check if all piles have only 1 stone
    all_ones = all(pile == 1 for pile in s)
    
    # Calculate XOR (nim sum) of all piles
    xor_sum = 0
    for pile in s:
        xor_sum ^= pile
    
    # Game logic for Misère Nim
    if all_ones:
        # If all piles have one stone, first wins only if number of piles is even
        return "First" if len(s) % 2 == 0 else "Second"
    else:
        # Otherwise, same as normal Nim: first wins if XOR != 0
        return "First" if xor_sum != 0 else "Second"


# Example test cases (no __main__, runs directly)
print(misereNim([1, 1]))       # Expected: First
print(misereNim([2, 1, 3]))    # Expected: Second
print(misereNim([1, 1, 1]))    # Expected: Second
print(misereNim([1, 1, 1, 1])) # Expected: First
