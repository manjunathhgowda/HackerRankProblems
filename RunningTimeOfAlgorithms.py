'''
Running Time of Algorithms

Given an array, count how many shifts occur during Insertion Sort.
A shift happens whenever an element is moved to the right.

Example:
Input:
5
2 1 3 1 2

Output:
4
'''

def runningTime(arr):
    shifts = 0
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]   # shift right
            shifts += 1
            j -= 1
        
        arr[j + 1] = key

    return shifts


# Example test (as HackerRank style, but not using input/output)
# print(runningTime([2,1,3,1,2]))  # Expected: 4
