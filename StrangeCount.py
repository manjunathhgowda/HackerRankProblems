'''
Strange Counter

There is a strange counter. At the first second, it displays 3. 
Each second, the number displayed by the counter decrements by 1 until it reaches 1. 
In the next second, the timer resets to double the previous starting value and continues counting down.

Cycle pattern:
Start = 3 → countdown to 1
Next start = 6 → countdown to 1
Next start = 12 → countdown to 1
... and so on (each cycle starting value doubles)

Given a time t, find the value displayed by the counter at that exact second.

Sample Input:
4

Sample Output:
6

Explanation:
At time t = 4, a new cycle starts with initial value 6.
'''

def strangeCounter(t):
    start = 3  # initial cycle length
    time = t

    # find the cycle where t belongs
    while time > start:
        time -= start
        start *= 2

    # value = start - (time - 1)
    return start - (time - 1)


# Example usage:
print(strangeCounter(4))   # Expected output: 6
print(strangeCounter(21))  # Another example → 1
print(strangeCounter(22))  # Another example → 12
