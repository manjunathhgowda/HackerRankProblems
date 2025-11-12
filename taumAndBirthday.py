'''
Problem: Taum and B'day

Taum is planning to celebrate the birthday of his friend, Diksha. 
There are two types of gifts that Diksha wants: black and white. 
To make her happy, Taum has to buy:
- b black gifts
- w white gifts.

The cost of:
- each black gift = bc
- each white gift = wc
- converting a gift from one color to another = z

Determine the minimum total cost of the gifts.

Example:
Input:
b = 3, w = 6
bc = 9, wc = 1, z = 1

Output:
12

Explanation:
He will buy 6 white gifts for 6×1 = 6.
For black gifts, he can convert white gifts at cost (1+1)=2 per gift.
So, total = 3×2 + 6×1 = 12.
'''

def taumBday(b, w, bc, wc, z):
    # If converting is cheaper than buying directly
    # For black gifts: min(bc, wc + z)
    # For white gifts: min(wc, bc + z)
    return (b * min(bc, wc + z)) + (w * min(wc, bc + z))

    #long method
    
    # if bc + z < wc:
    #     total_cost = (b * bc) + (w * (bc + z))
    #     return total_cost

    # # Case 2: If white gift + conversion is cheaper than black gift
    # # Then we can convert white gifts into black ones
    # elif wc + z < bc:
    #     total_cost = (b * (wc + z)) + (w * wc)
    #     return total_cost

    # # Case 3: Both gifts are already at minimum cost, no conversion needed
    # else:
    #     total_cost = (b * bc) + (w * wc)
    #     return total_cost


print(taumBday(10, 10, 1, 1, 1))   # Expected Output: 20
print(taumBday(5, 9, 2, 3, 4))     # Expected Output: 37
print(taumBday(3, 6, 9, 1, 1))     # Expected Output: 12
print(taumBday(7, 7, 4, 2, 1))     # Expected Output: 35
print(taumBday(3, 3, 1, 9, 2))     # Expected Output: 12
