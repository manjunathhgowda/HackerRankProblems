'''
Problem: Find Digits

An integer n is a divisor of itself if the remainder when n is divided by that digit is 0.

Given an integer n, for each digit that makes up n, determine whether it is a divisor. 
Count the number of divisors occurring within the integer.

Example:
n = 1012
The digits are 1, 0, 1, and 2.
n is evenly divisible by its digits 1, 1, and 2, but not by 0 (since division by zero is undefined).
So, the output is 3.

Function Description:
Complete the function findDigits below.

findDigits has the following parameter(s):
    int n: the value to analyze

Returns:
    int: the number of digits in n that are divisors of n

Constraints:
1 ≤ T ≤ 15
0 < n < 10^9

Sample Input:
2
12
1012

Sample Output:
2
3
'''

def findDigits(n):
    count = 0
    for digit in str(n):
        if digit != '0' and n % int(digit) == 0:
            count += 1
    return count


# Example usage (instead of main)
examples = [12, 1012, 12345, 100]
for num in examples:
    print(f"For {num} → Divisible digits count = {findDigits(num)}")
