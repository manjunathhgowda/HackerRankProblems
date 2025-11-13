'''
Priyanka and Toys

Priyanka works for an international toy company that ships by container. Her task is to determine 
the lowest cost way to combine her orders for shipping. She has a list of item weights. 
The shipping company has a requirement that all items loaded in a container must weigh 
less than or equal to 4 units plus the weight of the minimum weight item. 
All items meeting that requirement will be shipped in one container.

What is the smallest number of containers that can be contracted to ship the items 
based on the given list of weights?

Function Description:
Complete the 'toys' function below. 
It should return the minimum number of containers required to ship.

toys has the following parameter(s):
w: an array of integers that represent the weights of each order to ship

Input Format:
The first line contains an integer n, the number of orders to ship.
The next line contains n space-separated integers, w[i], representing the orders in a weight array.

Constraints:
1 <= n <= 10^5
0 <= w[i] <= 10^4

Output Format:
Return the integer value of the number of containers Priyanka must contract to ship all of the toys.

Sample Input:
8
1 2 3 21 7 12 14 21

Sample Output:
4

Explanation:
The first container holds items weighing 1, 2, 3, 7 (range 1–5)
The second container holds item 12 (range 12–16)
The third container holds items 14 (range 14–18)
The fourth container holds items 21, 21 (range 21–25)
So, 4 containers are required.
'''

def toys(w):
    w.sort()
    containers = 1
    min_weight = w[0]
    
    for weight in w:
        if weight > min_weight + 4:
            containers += 1
            min_weight = weight
    return containers


# Example usage:
print(toys([1, 2, 3, 21, 7, 12, 14, 21]))  # Expected Output: 4
