"""
Cats and a Mouse

Problem:
Given positions of two cats (A and B) and a mouse (C) on a line,
determine which cat will reach the mouse first.

If:
- Cat A reaches first → print "Cat A"
- Cat B reaches first → print "Cat B"
- Both reach at same time → print "Mouse C" (mouse escapes)

Function:
----------
catAndMouse(x, y, z)
    x → position of Cat A
    y → position of Cat B
    z → position of Mouse C
Returns → string ("Cat A", "Cat B", or "Mouse C")
"""

def catAndMouse(x, y, z):
    distA = abs(x - z)
    distB = abs(y - z)
    
    if distA < distB:
        return "Cat A"
    elif distB < distA:
        return "Cat B"
    else:
        return "Mouse C"

queries = [
    (1, 2, 3),  # Expected: Cat B
    (1, 3, 2),  # Expected: Mouse C
    (5, 2, 4),  # Expected: Cat B
    (3, 8, 6)   # Expected: Cat A
]

for x, y, z in queries:
    print(f"x={x}, y={y}, z={z} → {catAndMouse(x, y, z)}")

"""
Expected Output:
x=1, y=2, z=3 → Cat B
x=1, y=3, z=2 → Mouse C
x=5, y=2, z=4 → Cat B
x=3, y=8, z=6 → Cat A
"""
