#!/bin/python3

'''
Question:
Maria plays college basketball and wants to go pro. 
Each season she maintains a record of her play.
She tabulates the number of times she breaks her season record 
for most points and least points in a game.
Points scored in the first game establish her record for the season, 
and she begins counting from there.

Example:
Scores = [12, 24, 10, 24]

Count Table:
    Game  Score  Min  Max  MinCount  MaxCount
    0      12     12   12     0         0
    1      24     12   24     0         1
    2      10     10   24     1         1
    3      24     10   24     1         1

So output = [1, 1]  (1 time for most, 1 time for least)

Sample Input 0:
10 5 20 20 4 5 2 25 1

Sample Output 0:
2 4

Explanation:
- Broke best record 2 times (20 and 25)
- Broke worst record 4 times (5, 4, 2, 1)
=> Output: 2 4

Sample Input 1:
3 4 21 36 10 28 35 5 24 42

Sample Output 1:
4 0

Explanation:
- Broke best record 4 times
- Never broke worst record
=> Output: 4 0
'''

def breakingRecords(scores):
    min_score = max_score = scores[0]
    min_count = max_count = 0
    for score in scores[1:]:
        if score > max_score:
            max_score = score
            max_count += 1
        elif score < min_score:
            min_score = score
            min_count += 1
    return [max_count, min_count]

scores=[3,4,21,36,10,28,35,5,24,42]
print(breakingRecords(scores))

