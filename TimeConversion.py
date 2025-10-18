'''
Time Conversion Problem

Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

🕐 Note:
- 12:00:00AM → 00:00:00
- 12:00:00PM → 12:00:00

Examples:
1 Input: 07:05:45PM  → Output: 19:05:45
2 Input: 12:01:00PM  → Output: 12:01:00
3 Input: 12:01:00AM  → Output: 00:01:00

'''

def timeConversion(s):
    # Extract hour, minutes, seconds, and period (AM/PM)
    hour = int(s[0:2])
    minutes = s[3:5]
    seconds = s[6:8]
    period = s[8:]  # AM or PM

    if period == "AM":  # Convert to 24-hour format
        if hour == 12:
            hour = 0  # midnight case
    else:  # PM case
        if hour != 12:
            hour += 12  # add 12 for PM except 12PM
    # Format hour with leading zero if needed
    return f"{hour:02}:{minutes}:{seconds}"

print(timeConversion('07:05:45PM'))
print(timeConversion('12:01:00PM'))
print(timeConversion('12:01:00AM'))