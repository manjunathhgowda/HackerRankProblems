'''
HackerRank – The Time in Words

Given:
h = hour (1–12)
m = minutes (0–59)

Rules:
• If m == 0      → "<hour> o' clock"
• If m == 15     → "quarter past <hour>"
• If m == 30     → "half past <hour>"
• If m == 45     → "quarter to <next hour>"
• If 1 ≤ m < 30  → "<m in words> minute(s) past <hour>"
• If 30 < m < 60 → "<60-m in words> minute(s) to <next hour>"

Return the time in words.
'''

def timeInWords(h, m):

    words = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'quarter', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
        19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two',
        23: 'twenty three', 24: 'twenty four', 25: 'twenty five',
        26: 'twenty six', 27: 'twenty seven', 28: 'twenty eight',
        29: 'twenty nine', 30: 'half'
    }

    if m == 0:
        return f"{words[h]} o' clock"

    if m == 15:
        return f"quarter past {words[h]}"

    if m == 30:
        return f"half past {words[h]}"

    if m == 45:
        return f"quarter to {words[h+1 if h < 12 else 1]}"

    # General cases
    if m < 30:
        minute_word = "minute" if m == 1 else "minutes"
        return f"{words[m]} {minute_word} past {words[h]}"

    # m > 30 → "to next hour"
    remaining = 60 - m
    minute_word = "minute" if remaining == 1 else "minutes"
    next_hour = h + 1 if h < 12 else 1
    return f"{words[remaining]} {minute_word} to {words[next_hour]}"
print(timeInWords(5, 47))   # thirteen minutes to six
print(timeInWords(3, 0))    # three o' clock
print(timeInWords(7, 15))   # quarter past seven
