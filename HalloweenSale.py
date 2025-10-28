#!/bin/python3
"""
Halloween Sale

You wish to buy video games from an online store. The first game costs p dollars.
Every subsequent game costs d dollars less than the previous one, until the price
reaches m dollars; after that every game costs m dollars. Given a starting budget s,
determine how many games you can buy.

Function:
---------
howManyGames(p, d, m, s)
 - p: price of the first game
 - d: discount applied to the price for each subsequent game
 - m: minimum price a game can reach
 - s: starting budget

Return:
-------
Integer: number of games you can buy

Example:
--------
p=20, d=3, m=6, s=80  -> prices: 20,17,14,11,8,6,6,... -> you can buy 6 games
p=20, d=3, m=6, s=85  -> you can buy 7 games
"""

def howManyGames(p, d, m, s):
    count = 0
    price = p
    budget = s

    # buy while we have enough budget
    while budget >= price:
        budget -= price
        count += 1
        # decrease price but not below m
        price = max(m, price - d)

    return count


# Direct example calls (no __main__, no file I/O)
examples = [
    (20, 3, 6, 80),  # expected 6
    (20, 3, 6, 85),  # expected 7
    (100, 1, 1, 500) # some extra test
]

for p, d, m, s in examples:
    print(f"p={p}, d={d}, m={m}, s={s} -> {howManyGames(p, d, m, s)}")
