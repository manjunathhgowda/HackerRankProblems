'''
Problem: Smart Number

A number is called a smart number if it has an odd number of factors.
Given some numbers, determine whether each number is a smart number or not.

Example:
Input:
4
1
2
7
169

Output:
YES
NO
NO
YES

Explanation:
1 → factors = {1} → odd → YES  
2 → factors = {1,2} → even → NO  
7 → factors = {1,7} → even → NO  
169 → factors = {1,13,169} → odd → YES  
A number has an odd number of factors only if it is a perfect square.
'''

import math

def is_smart_number(num):
    val = int(math.sqrt(num))
    # ✅ FIXED LINE:
    if val * val == num:   # Perfect square check
        return True
    return False


# Example input (like HackerRank test)
test_cases = [1, 2, 7, 169]
for num in test_cases:
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")
