'''
HackerRank – Organizing Containers of Balls

You are given an n×n matrix "container" where:
• container[i][j] = number of balls of type j in container i

You can swap **any two balls between containers**.

Goal:
Determine if it is possible to rearrange balls so that:
1. Each container holds balls of exactly ONE type.
2. All balls of the same type end up in the same container.

Observation:
• We cannot change the total number of balls inside a container.
• We cannot change the total number of balls of each type.

Therefore:
Let A = list of total balls in each container  (row sums)
Let B = list of total balls for each ball type (column sums)

If sorted(A) == sorted(B):  return "Possible"
Else:                      return "Impossible"
'''

def organizingContainers(container):

    n = len(container)

    # Total balls in each container (row sums)
    row_sums = [sum(row) for row in container]

    # Total balls of each type (column sums)
    col_sums = [sum(container[i][j] for i in range(n)) for j in range(n)]

    # Only possible if both multisets match
    return "Possible" if sorted(row_sums) == sorted(col_sums) else "Impossible"


# -------------------
# Example Calls (no main)
# -------------------

print(organizingContainers([[1,1],[1,1]]))   # Possible
print(organizingContainers([[0,2],[1,1]]))   # Impossible

print(organizingContainers([
    [1,3,1],
    [2,1,2],
    [3,3,3]
]))  # Impossible

print(organizingContainers([
    [0,2,1],
    [1,1,1],
    [2,0,0]
]))  # Possible
