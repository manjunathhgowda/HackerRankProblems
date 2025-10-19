"""
HackerRank Problem: Mars Exploration

A space explorer’s ship crashed on Mars! They send a series of SOS messages to Earth for help.
However, some letters in the SOS messages are altered by cosmic radiation during transmission.

You are given the received signal `s` — determine how many letters differ from the expected "SOS" sequence.

Input Format:
    A single string, s.

Constraints:
    - 1 ≤ len(s) ≤ 99
    - s will contain only uppercase English letters (A–Z)

----------------------------------------------------------
Sample Input 0:
SOSSPSSQSSOR

Sample Output 0:
3

Explanation 0:
Received: SOSSPSSQSSOR
Expected:  SOSSOSSOSSOS
Differences:    X  X   X → 3 letters changed

----------------------------------------------------------
Sample Input 1:
SOSSOT

Sample Output 1:
1

Explanation 1:
Received: SOSSOT
Expected:  SOSSOS
Difference:        X → 1 letter changed

----------------------------------------------------------
Sample Input 2:
SOSSOSSOS

Sample Output 2:
0

Explanation 2:
All characters match the expected signal.
----------------------------------------------------------
"""

def marsExploration(s):
    expected = "SOS"
    changed_count = 0 
    for i in range(len(s)):
        if s[i] != expected[i % 3]:
            changed_count += 1    
    return changed_count
examples = [
    "SOSSPSSQSSOR",  # Expected output: 3
    "SOSSOT",         # Expected output: 1
    "SOSSOSSOS",      # Expected output: 0
    "SOOSSSOS"        # Expected output: 4
]
for signal in examples:
    print(marsExploration(signal))


