'''
HackerRank Problem: Counting Sort 1

Comparison Sorting:
Quicksort usually has a running time of O(n log n), but is there an algorithm that can sort even faster?
Counting sort does not require comparison. Instead, you create an integer array whose index range covers
the entire range of values in your array to sort. Each time a value occurs in the original array, you
increment the counter at that index. At the end, return this frequency array.

Example:
Input:
arr = [1, 1, 3, 2, 1]

Output:
[0, 3, 1, 1, 0, 0, 0, ..., 0]  # length = 100

Explanation:
arr contains:
- 1 occurs 3 times
- 2 occurs 1 time
- 3 occurs 1 time
The rest of the elements do not appear.

Function Description:
Complete the countingSort function below.
The function should return an integer array of length 100 representing frequencies.

Function Signature:
def countingSort(arr):

Constraints:
0 <= arr[i] < 100
1 <= n <= 10^6
'''

def countingSort(arr):
    # create a list of 100 zeros to count frequencies
    result = [0] * 100
    
    # increment count for each element
    for ele in arr:
        result[ele] += 1
        
    return result


# Example usage:
arr = [63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67,
       99, 12, 83, 89, 80, 91, 39, 86, 76, 85, 74, 39, 25, 90, 59, 10, 94, 32, 44, 3,
       89, 30, 27, 79, 46, 96, 27, 32, 18, 21, 92, 69, 81, 40, 40, 34, 68, 78, 24, 87,
       42, 69, 23, 41, 78, 22, 6, 90, 99, 89, 50, 30, 20, 1, 43, 3, 70, 95, 33, 46, 44,
       9, 69, 48, 33, 60, 65, 16, 82, 67, 61, 32, 21, 79, 75, 75, 13, 87, 70, 33]

print(countingSort(arr))
