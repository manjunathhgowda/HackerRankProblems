'''
Happy Ladybugs
---------------
A ladybug is happy if it sits next to another ladybug of the same color.
We can move ladybugs into empty '_' cells any number of times.

Rules:
1. If there is any color with only one ladybug, it's impossible → NO.
2. If there are no empty cells, check if all ladybugs are already happy.
3. Otherwise, if there’s at least one '_', and all colors appear ≥ 2 times → YES.

Example:
Input:
4
7
RBY_YBR
6
X_Y__X
2
__
6
B_RRBR

Output:
YES
NO
YES
YES
'''

def happyLadybugs(b):
    # Case 1: Only one cell
    if len(b) == 1:
        return "YES" if b == "_" else "NO"

    # Count each character
    counts = {}
    for ch in b:
        counts[ch] = counts.get(ch, 0) + 1

    # Case 2: If no underscore and unhappy ladybugs exist
    if "_" not in b:
        for i in range(len(b)):
            if (i > 0 and b[i] == b[i-1]) or (i < len(b)-1 and b[i] == b[i+1]):
                continue
            else:
                return "NO"
        return "YES"

    # Case 3: If any ladybug color appears only once
    for k, v in counts.items():
        if k != "_" and v == 1:
            return "NO"

    # Otherwise possible to rearrange and make all happy
    return "YES"
# Example usage
print(happyLadybugs("RBY_YBR"))   # YES
print(happyLadybugs("X_Y__X"))    # NO
print(happyLadybugs("__"))        # YES
print(happyLadybugs("B_RRBR"))    # YES
