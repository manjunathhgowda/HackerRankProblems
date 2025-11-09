'''
Problem: Chocolate Feast

Little Bobby loves chocolate. He frequently goes to his favorite store, Penny Auntie, to buy them. 
They are having a promotion at Penny Auntie. If Bobby saves enough wrappers, he can turn them in for a free chocolate.

Example:
He has  n = 10  to spend, bars cost  c = 2 , and he can turn in  m = 5  wrappers to receive another bar. 
Initially, he buys 5 bars and has 5 wrappers after eating them. He turns in 5 wrappers for 1 more bar. 
After eating that one, he has 1 wrapper left, and his feast ends. 
Overall, he has eaten 6 bars.

Function Description:

Complete the function chocolateFeast below.
The function returns an INTEGER - the total number of chocolates Bobby can eat.

chocolateFeast has the following parameters:
    int n: Bobby's initial amount of money
    int c: the cost of a chocolate bar
    int m: the number of wrappers he can turn in for a free bar

Input Format:
n c m - three integers representing money, cost, and wrapper trade rate.

Constraints:
1 ≤ n, c, m ≤ 1000

Sample Input:
10 2 5

Sample Output:
6
'''

def chocolateFeast(n, c, m):
    chocolates = n // c
    wrappers = chocolates
    while wrappers >= m:
        new_chocolates = wrappers // m
        chocolates += new_chocolates
        wrappers = wrappers % m + new_chocolates
    return chocolates

print(chocolateFeast(10, 2, 5))  # Expected output: 6
print(chocolateFeast(12, 4, 4))  # Expected output: 3
print(chocolateFeast(6, 2, 2))   # Expected output: 5
