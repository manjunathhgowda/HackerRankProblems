
'''
Question:
An avid hiker keeps meticulous records of their hikes. 
During the last hike that consisted of exactly 'steps' steps, for every step it was noted if it was an uphill (U) or a downhill (D) step. 
Hikes always start and end at sea level. Each step up or down represents a 1 unit change in altitude.

Definitions:
- A mountain is a sequence of consecutive steps above sea level, starting with an up step from sea level and ending with a down step to sea level.
- A valley is a sequence of consecutive steps below sea level, starting with a down step from sea level and ending with an up step to sea level.

Given the sequence of up and down steps during a hike, find the number of valleys traversed.

Example:
steps = 8
path = "UDDDUDUU"

The hiker enters and leaves one valley.


Parameters:
    steps: INTEGER → number of steps in the hike
    path: STRING → string describing the path ('U' or 'D')

Returns:
    INTEGER → number of valleys traversed
'''

def countingValleys(steps, path):
    current_level = 0
    valleys = 0
    for step in path:
        if step == 'U':
            current_level += 1
            # If we just came up to sea level, a valley ended
            if current_level == 0:
                valleys += 1
        elif step == 'D':
            current_level -= 1
    return valleys
print(countingValleys(8, "UDDDUDUU"))