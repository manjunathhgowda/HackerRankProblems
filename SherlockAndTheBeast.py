'''
Sherlock and The Beast
----------------------
A Decent Number has the following properties:
1. Its digits are only 3’s and/or 5’s.
2. The number of 3’s it contains is divisible by 5.
3. The number of 5’s it contains is divisible by 3.
4. It must be the largest such number for the given length n.

Given n (the number of digits), print the largest decent number of that length,
or -1 if no such number exists.

Example:
Input:
3
1
3
5
Output:
-1
555
33333
'''

def decentNumber(n):
    # Start with maximum number of 5’s (since 5 > 3 gives a larger number)
    fives = n
    while fives % 3 != 0:
        fives -= 5  # Reduce 5's count by 5 until divisible by 3
    if fives < 0:
        print(-1)
    else:
        threes = n - fives
        print('5' * fives + '3' * threes)


# Example usage
decentNumber(1)   # Output: -1
decentNumber(3)   # Output: 555
decentNumber(5)   # Output: 33333
decentNumber(11)  # Output: 55555533333
