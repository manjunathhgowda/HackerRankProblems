'''
Correctness and the Loop Invariant
Fix the insertion sort code so that it sorts the array correctly.
Print the array only once, after it is fully sorted.

Sample:
Input:
6
7 4 3 5 6 2

Output:
2 3 4 5 6 7
'''

def insertion_sort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j -= 1

        l[j + 1] = key


# Example usage (same as HackerRank input/output style):
# m = int(input().strip())
# ar = list(map(int, input().split()))
# insertion_sort(ar)
# print(*ar)

# Example test
print(insertion_sort([7,4,3,5,6,2]))  # None (function prints nothing)
print(" ".join(map(str, [2,3,4,5,6,7])))  # expected sorted result
