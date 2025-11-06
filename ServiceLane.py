'''
Service Lane

A driver is driving on the freeway. The check engine light of his vehicle is on, 
and the driver wants to get service immediately. Luckily, a service lane runs parallel 
to the highway. It varies in width along its length.

You will be given an array of widths at points along the road (indices), then a list of 
the indices of entry and exit points. Considering each entry and exit point pair, 
calculate the maximum size vehicle that can travel that segment of the service lane safely.

Example:

width = [2, 3, 1, 2, 3, 2, 3, 3]
cases = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]

For the first case [0, 3], the segment widths are [2, 3, 1, 2]. The widest vehicle that can 
fit through all segments is 1.

Function Description:

Complete the serviceLane function in the editor below.

serviceLane has the following parameter(s):
    int n: the size of the width array
    2D_INTEGER_ARRAY cases: each element contains the starting and ending indices for a segment to consider

Returns:
    INTEGER_ARRAY: the maximum width vehicle that can pass through each segment of the service lane described
'''

def serviceLane(n, cases, width):
    result = []

    # Loop over all test cases
    for i in range(len(cases)):
        entry = cases[i][0]
        exit = cases[i][1]
        min_width = width[entry]  # start with the first width in the segment

        # Loop through the segment to find the minimum width
        for j in range(entry, exit + 1):
            if width[j] < min_width:
                min_width = width[j]

        result.append(min_width)

    return result

width = [2, 3, 1, 2, 3, 2, 3, 3]
cases = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]
print(serviceLane(len(width), cases, width))  # Output: [1, 2, 3, 2, 1]
