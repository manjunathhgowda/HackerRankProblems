'''
HackerRank - Counting Sort 2

Given an unsorted list of integers (0–99),
perform counting sort and return the sorted list.

Example:
arr = [1, 1, 3, 2, 1]

Counting array = [0,3,1,1]
Sorted output = [1,1,1,2,3]
'''

def countingSort(arr):
    count = [0] * 100
    
    # count occurrences
    for num in arr:
        count[num] += 1
    
    # build sorted result
    result = []
    for value in range(100):
        result.extend([value] * count[value])
    
    return result

    # return sorted(arr)


# Example call
print(countingSort([63, 25, 73, 1, 98, 73, 56]))
