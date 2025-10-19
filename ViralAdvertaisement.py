#!/bin/python3
"""
Viral Advertising

Problem:
Each day, the advertisement is shared with a certain number of people.
Half of them (rounded down) like the ad and share it with 3 new friends the next day.

We must find the total cumulative likes after 'n' days.

Example:
Day 1: shared = 5 → liked = 2 → total = 2
Day 2: shared = 6 → liked = 3 → total = 5
Day 3: shared = 9 → liked = 4 → total = 9
Output = 9
"""

def viralAdvertising(n):
    # Initial number of people who receive the ad
    shared = 5
    total_likes = 0
    # Loop through each day
    for day in range(1, n + 1):
        liked = shared // 2           # Half of them like the ad
        total_likes += liked          # Add to total likes
        shared = liked * 3            # Each liker shares with 3 friends
    return total_likes
# You can test directly like this:
print(viralAdvertising(3))   # Expected output: 9
print(viralAdvertising(5))   # Expected output: 24
