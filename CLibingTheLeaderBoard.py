'''
HackerRank – Climbing the Leaderboard

The leaderboard uses Dense Ranking:

• Highest score ⇒ Rank 1
• Equal scores ⇒ Same rank
• Next different score ⇒ Next rank number

You are given:
ranked = existing leaderboard scores (descending)
player = Alice's game scores (ascending)

For each score in player, return Alice's rank.

Example:
ranked = [100, 90, 90, 80]
player  = [70, 80, 105]

Output: [4, 3, 1]
'''

def climbingLeaderboard(ranked, player):
    # Remove duplicates from ranked
    unique = []
    for score in ranked:
        if not unique or unique[-1] != score:
            unique.append(score)

    # Two-pointer: start from bottom of leaderboard
    idx = len(unique) - 1
    result = []

    for score in player:
        # climb up while player score >= leaderboard score
        while idx >= 0 and score >= unique[idx]:
            idx -= 1

        # rank = idx+2 because:
        # if idx = -1 -> rank 1
        # if idx = 0  -> rank 2 (one score beaten)
        result.append(idx + 2)

    return result

ranked_example = [100, 90, 90, 80, 75, 60]
player_example = [50, 65, 77, 90, 102]

print(climbingLeaderboard(ranked_example, player_example))
# Expected: [6, 5, 4, 2, 1]
