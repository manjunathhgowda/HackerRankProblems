'''
HackerRank - Jim and the Orders

Jim's Burgers has a line of hungry customers. Orders vary in the time
it takes to prepare them. You are given the order number and preparation
time for each customer in line (customer numbers start from 1).

The serve time for a customer is:
    serve_time = order_number + prep_time

Customers must be served in ascending order of their serve time.
If two customers have the same serve time, serve the one with the
smaller customer number first.

Function Description:
---------------------
Complete the function jimOrders(orders).

jimOrders has the following parameter:
    orders: a 2D list, where each element is [order_number, prep_time]

Returns:
    A list of integers representing customer numbers in the order they
    receive their orders.

Example:
Input:
3
1 3
2 3
3 3

Output:
1 2 3

Explanation:
Customer 1: serve at 4
Customer 2: serve at 5
Customer 3: serve at 6
Thus served in the same order.

Constraints:
1 <= n <= 10^5
1 <= order_number, prep_time <= 10^6
'''
def jimOrders(orders):
    serve = []

    for i, (order, prep) in enumerate(orders, start=1):
        serve.append((order + prep, i))  # (serve_time, customer_number)

    serve.sort()  # sorts by serve_time, then customer_number automatically

    return [cust for _, cust in serve]


# ------ Example Calls (Instead of main) ----------
print(jimOrders([[1, 3], [2, 3], [3, 3]]))
# Expected: [1, 2, 3]

print(jimOrders([[8, 1], [4, 2], [5, 6], [3, 1], [4, 3]]))
# Expected: [4, 2, 5, 1, 3]
