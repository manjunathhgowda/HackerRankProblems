'''
Question:
There is a large pile of socks that must be paired by color. 
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.

Example:
Input:
9
10 20 20 10 10 30 50 10 20

Output:
3
'''

def sockMerchant(n, ar):
    pairs = 0
    colors = set()  # to track unpaired socks
    for sock in ar:
        if sock in colors:
            pairs += 1      # found a pair
            colors.remove(sock)
        else:
            colors.add(sock)
    return pairs

# Example usage
n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(n, ar))  # Output: 3
