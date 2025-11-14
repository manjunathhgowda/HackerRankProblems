'''
Cavity Map

You are given a square map as a matrix of integer strings. Each cell of the map has a value denoting its depth. 
We will call a cell of the map a cavity if and only if this cell is not on the border of the map and 
each cell adjacent to it has strictly smaller depth. Two cells are adjacent if they share a common side (up, down, left, right).

Find all the cavities on the map and replace their depths with the uppercase character 'X'.

Example:
Input:
989
191
111

Output:
989
1X1
111

Explanation:
The center cell (depth 9) is not on the border and is deeper than all its adjacent cells [8,1,1,1].
Hence, it is replaced by 'X'.

Function Description:
Complete the 'cavityMap' function below.

Parameters:
string grid[n]: each string represents a row of the grid

Returns:
string[n]: the modified grid

Sample Input:
4
1112
1912
1892
1234

Sample Output:
1112
1X12
18X2
1234
'''

def cavityMap(grid):
    grid = [list(row) for row in grid]
    n = len(grid)
    
    for i in range(1, n-1):
        for j in range(1, n-1):
            current = grid[i][j]
            if (grid[i-1][j] < current and grid[i+1][j] < current and
                grid[i][j-1] < current and grid[i][j+1] < current):
                grid[i][j] = 'X'
    
    return [''.join(row) for row in grid]


# Example usage:
example = ['1112', '1912', '1892', '1234']
result = cavityMap(example)
for line in result:
    print(line)

# Expected Output:
# 1112
# 1X12
# 18X2
# 1234
