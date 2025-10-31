"""
Utopian Tree

The Utopian Tree goes through two growth cycles every year:
- In spring, it doubles in height.
- In summer, it increases its height by 1 meter.

Given the number of growth cycles `n`, return the final height of the tree.
"""

# Complete the 'utopianTree' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.

def utopianTree(n):
    height = 1  # Initial height
    for i in range(n):
        if i % 2 == 0:   # Spring cycle (even index)
            height *= 2
        else:             # Summer cycle (odd index)
            height += 1
    return height

examples = [0, 1, 4]

for n in examples:
    print(utopianTree(n))
