'''
Question:
A teacher asks the class to open their books to a page number. 
A student can start turning pages from the front or the back of the book. 
They always turn pages one at a time. 
Page 1 is always on the right side when the book is opened.

Given the total number of pages `n` and the page number `p` the student wants to reach, 
calculate the minimum number of pages that must be turned.

Example:
n = 6, p = 2
- From the front: turn 1 page → reach page 2
- From the back: turn 2 pages → reach page 2
Minimum turns = 1
'''
def pageCount(n, p):
    from_front = p // 2 # Pages turned from the front
    from_back = (n // 2) - (p // 2) # Pages turned from the back, If n is even, last sheet may contain n-1 and n
    return min(from_front, from_back)       # Minimum of the two
print(pageCount(6,2))
