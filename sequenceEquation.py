"""
Sequence Equation

Problem:
---------
You are given a permutation p of the integers from 1 to n.
For each x in [1, n], find y such that p[p[y]] = x.
Return the sequence of all such y values.

Example:
---------
p = [2, 3, 1]

For x = 1 → p[y] = 1 → y = 3 → p[p[y]] = 1 → output = 2  
For x = 2 → p[y] = 2 → y = 1 → output = 3  
For x = 3 → p[y] = 3 → y = 2 → output = 1  

Output: [2, 3, 1]
"""

def permutationEquation(p):
    result_lst=[]
    for x in range(1, len(p) + 1):
        y = p.index(x) + 1   
        z = p.index(y) + 1
        result_lst.append(z)
    return result_lst
example1 = [2, 3, 1]
example2 = [4, 3, 5, 1, 2]

print("Input:", example1)
print("Output:", *permutationEquation(example1))  # Expected: 2 3 1

print("Input:", example2)
print("Output:", *permutationEquation(example2))  # Expected: 1 3 5 4 2
