#!/bin/python3

'''
Question:
You are in charge of the cake for a child's birthday. 
It will have one candle for each year of their total age. 
They will only be able to blow out the tallest candles. 
Your task is to count how many candles are the tallest.

Example:
candles = [4, 4, 1, 3]
The tallest candles are 4 units high. There are 2 of them.
So, the function should return 2.
Parameters:
    candles: an array of integers representing candle heights
    Returns: The number of candles that are tallest.
Sample Input:
3 2 1 3
Sample Output:
2
Explanation:The tallest candle height is 3, and there are two of them 
(the first and the last candle). Hence, output is 2.
'''

def birthdayCakeCandles(candles):
    tallest = max(candles)
    count = candles.count(tallest)
    return count
candles=[3,2,1,3]
print(birthdayCakeCandles(candles))