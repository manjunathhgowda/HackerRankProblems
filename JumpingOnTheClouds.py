'''
HackerRank Challenge: Jumping on the Clouds

Problem Description:
--------------------
You are playing a game where you jump across clouds.
Each cloud is either:
- 0 (cumulus cloud, safe)
- 1 (thunderhead, must be avoided)

You start from the first cloud (index 0) and must reach the last cloud.
You can jump to:
- the next cloud (index +1)
- or skip one cloud (index +2)
...but only if that cloud is safe (value 0).

Task:
-----
Find the minimum number of jumps required to reach the last cloud.

Function Description:
---------------------
Complete the function jumpingOnClouds below.

jumpingOnClouds has the following parameter:
- int c[n]: array of binary integers representing safe (0) or unsafe (1) clouds.

Returns:
- int: minimum number of jumps to reach the last cloud.

Input Format:
-------------
The first line contains an integer n — number of clouds.
The second line contains n space-separated integers (each either 0 or 1).

Constraints:
------------
2 ≤ n ≤ 100
c[i] ∈ {0, 1}
There will always be at least one path to reach the end.

Sample Input 0:
---------------
7
0 0 1 0 0 1 0

Sample Output 0:
----------------
4

Explanation 0:
---------------
Path: 0 → 1 → 3 → 4 → 6
Jumps: (2), (2), (1), (2) → total = 4

Sample Input 1:
---------------
6
0 0 0 0 1 0

Sample Output 1:
----------------
3

Explanation 1:
---------------
Path: 0 → 2 → 3 → 5
Jumps = 3
'''

def jumpingOnClouds(c):
    jumps = 0
    i = 0
    n = len(c)
    
    # Greedy approach: always jump 2 if possible, else jump 1
    while i < n - 1:
        if i + 2 < n and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
    return jumps
print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))  # Expected: 4
print(jumpingOnClouds([0, 0, 0, 0, 1, 0]))     # Expected: 3
print(jumpingOnClouds([0, 0]))                 # Expected: 1
