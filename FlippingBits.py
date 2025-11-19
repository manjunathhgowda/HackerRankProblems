'''
Flipping Bits - HackerRank Solution

Given a 32-bit unsigned integer n, flip all bits and return the result.
We use XOR with 0xFFFFFFFF (which is 32 bits of all 1s).
'''

def flippingBits(n):
    return n ^ 0xFFFFFFFF
# ---- Example Test Calls ----
print(flippingBits(2147483647))   # Expected: 2147483648
print(flippingBits(1))            # Expected: 4294967294
print(flippingBits(0))            # Expected: 4294967295
print(flippingBits(4))            # Expected: 4294967291
print(flippingBits(123456))       # Expected: 4294843839
