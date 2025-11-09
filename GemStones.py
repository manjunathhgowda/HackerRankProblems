'''
HackerRank Problem: Gemstones

There is a collection of rocks where each rock has various minerals embedded in it. 
Each type of mineral is designated by a lowercase letter in the range 'a'–'z'. 
A mineral is called a "gemstone" if it occurs at least once in each of the rocks.

Given a list of strings where each string represents a rock and its minerals, 
determine how many types of gemstones there are.

Example:
----------
Input:
    arr = ['abcdde', 'baccd', 'eeabg']
Output:
    2

Explanation:
    The minerals 'a' and 'b' appear in every rock, so there are 2 gemstones.

Function Description:
---------------------
Complete the function 'gemstones' below.

gemstones has the following parameter(s):
    string arr[n]: an array of strings

Returns:
    int: the number of gemstones found

Constraints:
    1 <= n <= 100
    1 <= |arr[i]| <= 100
    arr[i] consists of only lowercase Latin letters ('a'-'z')
'''

def gemstones(arr):
    # Convert the first rock to a set of minerals
    common_minerals = set(arr[0])

    # For each remaining rock, intersect its minerals with the common set
    for rock in arr[1:]:
        common_minerals &= set(rock)

    # The number of remaining minerals is the number of gemstones
    return len(common_minerals)


# Example usage (no main block)
example_arr = ['abcdde', 'baccd', 'eeabg']
print(gemstones(example_arr))  # Expected Output: 2
