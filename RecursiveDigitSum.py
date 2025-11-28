'''
HackerRank Problem: Recursive Digit Sum

We define super digit of an integer using the rules:

- If n has only 1 digit → super digit = n
- Otherwise → super digit = superDigit(sum of digits of n)

The number P is formed by concatenating string n, k times.

Key Optimization:
Instead of forming the huge string n*k,
super digit = superDigit( sum_of_digits(n) * k )

Your task:
Implement superDigit(n, k) and return the final super digit.
'''

def superDigit(n, k):

    # Convert n to sum of digits
    initial_sum = sum(int(d) for d in n)

    # Multiply by k (instead of repeating the string)
    total = initial_sum * k

    # Recursive helper function
    def helper(x):
        if x < 10:
            return x
        s = sum(int(d) for d in str(x))
        return helper(s)

    return helper(total)


# Example calls (as requested, no main)
print(superDigit("148", 3))   # Expected 3
print(superDigit("9875", 4))  # Expected 8
print(superDigit("123", 3))   # Expected 9
