'''
Luck Balance

Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests.
Initially, her luck balance is 0. Each contest is described by two integers: L[i] and T[i]:

    - L[i]: the amount of luck associated with a contest.
      If Lena wins, her luck decreases by L[i]; if she loses, it increases by L[i].
    - T[i]: the contest's importance rating (1 = important, 0 = unimportant).

If Lena can lose no more than K important contests, what is the maximum amount of luck she can have after competing
in all contests?

Example:
-----------
K = 3
contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]

Output → 29

Explanation:
There are 6 contests, 4 are important, and she can lose 3 of them.
She should win the smallest important contest (1), and lose all others.

Total Luck = (5 + 2 + 8 + 10 + 5) - 1 = 29

Function Description:
---------------------
Complete the luckBalance function below.

luckBalance has the following parameters:
    int k: the maximum number of important contests Lena can lose
    int contests[n][2]: each contest's luck and importance

Returns:
    int: the maximum luck balance achievable

Constraints:
    1 <= n <= 100
    0 <= k <= n
    1 <= L[i] <= 10^4
    T[i] ∈ {0, 1}
'''

def luckBalance(k, contests):
    # Separate important and unimportant contests
    important = []
    total_luck = 0

    for luck, importance in contests:
        if importance == 1:
            important.append(luck)
        else:
            total_luck += luck  # Always lose unimportant contests

    # Sort important contests by luck in descending order
    important.sort(reverse=True)

    # Lose k most valuable important contests
    total_luck += sum(important[:k])

    # Win the rest (subtract their luck)
    total_luck -= sum(important[k:])

    return total_luck

print(luckBalance(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]))  # Output: 29
print(luckBalance(2, [[5, 1], [1, 1], [4, 0]]))                          # Output: 10
print(luckBalance(0, [[5, 1], [2, 1], [1, 1]]))                          # Output: -8
