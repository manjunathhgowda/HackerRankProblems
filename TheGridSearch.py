'''
HackerRank Problem: The Grid Search

You are given a grid G of R rows, each row a string of digits.
You are also given a pattern P of r rows.

A pattern P is said to be found inside G if:
- There exists a starting row i and starting column j
- Such that for every row k of P,
  P[k] matches G[i+k] starting at column j.

Return "YES" if the pattern exists in the grid, otherwise "NO".

Approach:
- For each row in G:
    - Try to locate the first row of P inside it using substring search.
    - When found, check the next rows to see if all pattern rows match.
- If a complete match is found → return YES
- Otherwise, return NO
'''

def gridSearch(G, P):
    R = len(G)
    C = len(G[0])
    r = len(P)
    c = len(P[0])

    # Loop through all possible starting rows
    for i in range(R - r + 1):

        # Find all occurrences of P[0] in G[i]
        start = 0
        while True:
            pos = G[i].find(P[0], start)  # substring search
            if pos == -1:
                break  # no more matches in this row

            # Check remaining rows of pattern
            match = True
            for k in range(1, r):
                if G[i + k][pos:pos + c] != P[k]:
                    match = False
                    break

            if match:
                return "YES"

            start = pos + 1  # search next occurrence

    return "NO"


# Example calls (NO main, as requested)
print(gridSearch(
    [
        "7283455864",
        "6731158619",
        "8988242643",
        "3830589324",
        "2229505813",
        "5633845374",
        "6473530293",
        "7053106601",
        "0834282956",
        "4607924137"
    ],
    [
        "9505",
        "3845",
        "3530"
    ]
))  # Expected YES

print(gridSearch(
    [
        "400453592126560",
        "114213133098692",
        "474386082879648",
        "522356951189169",
        "887109450487496",
        "252802633388782",
        "502771484966748",
        "075975207693780",
        "511799789562806",
        "404007454272504",
        "549043809916080",
        "962410809534811",
        "445893523733475",
        "768705303214174",
        "650629270887160"
    ],
    [
        "99",
        "99"
    ]
))  # Expected NO
