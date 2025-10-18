'''
Question:
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated integers.

Example:
arr = [1, 2, 3, 4, 5]
- Sum of all except 1 → 2+3+4+5 = 14 (max)
- Sum of all except 5 → 1+2+3+4 = 10 (min)

Output:
10 14
'''

def miniMaxSum(arr):
    total_sum = sum(arr)                # Total sum of all elements
    min_sum = total_sum - max(arr)      # Minimum sum: total sum minus the maximum element
    max_sum = total_sum - min(arr)      # Maximum sum: total sum minus the minimum element
    print(f"{min_sum} {max_sum}")
arr =[1, 2, 3, 4, 5] 
miniMaxSum(arr)
