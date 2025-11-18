'''
HackerRank - Insertion Sort - Part 2

You must sort the array using insertion sort.
After placing each element in its correct position,
print the entire array.

Example:
Input:
6
1 4 3 5 6 2

Output:
1 4 3 5 6 2
1 3 4 5 6 2
1 3 4 5 6 2
1 3 4 5 6 2
1 2 3 4 5 6
'''

def insertionSort2(n, arr):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # shift bigger elements to right
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key
        
        # print in required format
        print(*arr)

# Example call
insertionSort2(6, [1, 4, 3, 5, 6, 2])
