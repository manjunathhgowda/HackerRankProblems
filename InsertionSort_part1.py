'''
Insertion Sort - Part 1

Given a sorted array except for the last element (arr[n-1]), insert this last unsorted element 
into its correct position by shifting elements to the right. After each shift, print the array.

You stop when the correct position for the unsorted element is found, then insert it and print.

Example:
Input:
5
2 4 6 8 3

Output:
2 4 6 8 8 
2 4 6 6 8 
2 4 4 6 8 
2 3 4 6 8 
'''

def insertionSort1(n, arr):
    key = arr[-1]  # unsorted value
    i = n - 2

    # shift values to right until correct position found
    while i >= 0 and arr[i] > key:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1

    # insert the key
    arr[i + 1] = key
    print(*arr)


# Example usage:
insertionSort1(5, [2, 4, 6, 8, 3])
