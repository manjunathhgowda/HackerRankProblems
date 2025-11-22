'''
HackerRank – Encryption

Given a string s:
1. Remove all spaces.
2. Let L = len(s).
3. Compute:
      rows = floor(sqrt(L))
      cols = ceil(sqrt(L))
4. If rows * cols < L, increase rows by 1.
5. Write the string in a grid of rows x cols.
6. Read the grid column-wise, joining each column with a space.

Return the encrypted string.

Example:
s = "haveaniceday"
Grid:
have
anic
eday
Output:
"hae and via ecy"
'''

def encryption(s):
    # remove spaces
    s = s.replace(" ", "")
    L = len(s)

    import math
    r = int(math.floor(math.sqrt(L)))
    c = int(math.ceil(math.sqrt(L)))

    if r * c < L:
        r += 1

    # build grid row-wise
    grid = [s[i:i+c] for i in range(0, L, c)]

    # read by columns
    result = []
    for col in range(c):
        word = ""
        for row in grid:
            if col < len(row):
                word += row[col]
        result.append(word)

    return " ".join(result)

print(encryption("haveaniceday"))   # hae and via ecy
print(encryption("feedthedog"))     # fto ehg ee dd
print(encryption("chillout"))       # clu hlt io
print(encryption("if man was meant to stay on the ground god would have given us roots"))
# imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau
