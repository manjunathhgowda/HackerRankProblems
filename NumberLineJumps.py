'''
Question:
You are choreographing a circus show with various animals. 
For one act, you are given two kangaroos on a number line 
ready to jump in the positive direction (i.e., toward positive infinity).

The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.

You need to determine if both kangaroos will ever land at the same location after making the same number of jumps.

Function Description:
Complete the function 'kangaroo' below.

Parameters:
    int x1, v1: starting position and jump distance for kangaroo 1
    int x2, v2: starting position and jump distance for kangaroo 2

Returns:
    string: "YES" if they can meet, otherwise "NO"

Input Format:
    A single line of four space-separated integers: x1 v1 x2 v2

Constraints:
    0 <= x1 < x2 <= 10000
    1 <= v1 <= 10000
    1 <= v2 <= 10000

Sample Input 0:
0 3 4 2

Sample Output 0:
YES

Explanation 0:
The two kangaroos jump through the following sequence of locations:
Kangaroo 1: 0 → 3 → 6 → 9 → 12
Kangaroo 2: 4 → 6 → 8 → 10 → 12
Both meet at location 12 after 4 jumps. So, print "YES".

Sample Input 1:
0 2 5 3

Sample Output 1:
NO

Explanation 1:
Kangaroo 2 starts ahead (x2 > x1) and also jumps faster (v2 > v1),
so Kangaroo 1 will never catch up. Therefore, print "NO".
'''
def kangaroo(x1, v1, x2, v2):
    # If the second kangaroo jumps faster and is already ahead, they can never meet
    if v2 >= v1 and x2 > x1:
        return "NO"
    # Check mathematically if they meet at the same point
    # (x1 + n*v1) == (x2 + n*v2) → n = (x2 - x1) / (v1 - v2)
    # They meet only if n is a non-negative integer
    if (v1 != v2) and (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    else:
        return "NO"
print(kangaroo(0,3,4,2))
