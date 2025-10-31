"""
Beautiful Binary String

Alice thinks a binary string is beautiful if it does NOT contain the substring "010".
In one step, she can change any '0' to '1' or '1' to '0'.

Find the minimum number of steps to make the string beautiful.
"""

def beautifulBinaryString(b):
    count = 0
    i = 0
    while i < len(b) - 2:
        if b[i:i+3] == '010':
            count += 1
            i += 3  
        else:
            i += 1
    return count
examples = [
    "0101010",     # Expected output: 2
    "01100",       # Expected output: 0
    "0100101010"   # Expected output: 3
]

for b in examples:
    print(beautifulBinaryString(b))
