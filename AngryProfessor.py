"""
Angry Professor

Problem:
---------
A professor cancels class if fewer than 'k' students arrive on time.
Arrival time <= 0 → on time or early
Arrival time > 0  → late

Return:
'YES' → class is cancelled
'NO'  → class is not cancelled
"""

def angryProfessor(k, a):
    ontime=0
    for ele in a:
        if ele<=0:
            ontime+=1
    if ontime<k:
        return 'YES'
    else:
        return 'NO'

example1 = [-1, -3, 4, 2]   # 2 on time, threshold 3 → YES (cancelled)
example2 = [0, -1, 2, 1]    # 2 on time, threshold 2 → NO (not cancelled)

print("Example 1 Output:", angryProfessor(3, example1))  # Expected: YES
print("Example 2 Output:", angryProfessor(2, example2))  # Expected: NO
