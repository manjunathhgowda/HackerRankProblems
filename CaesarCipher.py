
'''
Caesar Cipher Problem 

We shift every letter by 'k' positions.
If we reach the end of the alphabet, we wrap around to the beginning.
Uppercase and lowercase letters are handled separately.

Example:
Input:
middle-Outz
2
Output:
okffng-Qwvb
'''
import os

def caesarCipher(s, k):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    k = k % 26  # in case k > 26
    r_lower = lower[k:] + lower[:k]       
    r_upper = upper[k:] + upper[:k]       
    new_s = ""

    for ch in s:
        if ch in lower:                   
            idx = lower.index(ch)
            new_s += r_lower[idx]
        elif ch in upper:                 
            idx = upper.index(ch)
            new_s += r_upper[idx]
        else:                             
            new_s += ch

    return new_s

print(caesarCipher('middle-Outz',2))