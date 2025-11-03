'''
When a contiguous block of text is selected in a PDF viewer, the selection is highlighted 
with a blue rectangle. In this PDF viewer, each word is highlighted independently.

There is a list of 26 character heights aligned by index to their letters. 
For example, 'a' is at index 0 and 'z' is at index 25. There will also be a string.
Using the letter heights given, determine the area of the rectangle highlight 
in square millimeters assuming all letters are 1mm wide.

Example:
heights = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
word = "abc"
The tallest letter is 'b' with height 3 and word length is 3
→ Area = 3 * 3 = 9

Function Description:
Complete the function designerPdfViewer below.

designerPdfViewer has the following parameter(s):
    int h[26]: the heights of each letter
    string word: a string

Returns:
    int: the size of the highlighted area

Constraints:
    Each height is between 1 and 7 inclusive
    word contains only lowercase English letters

Sample Input 0:
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
abc

Sample Output 0:
9

Sample Input 1:
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
zaba

Sample Output 1:
28
'''

def designerPdfViewer(h, word):
    # Using alphabet string instead of ASCII
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    max_height = 0

    for i in range(len(word)):
        # find letter index using loop
        for j in range(len(alphabet)):
            if word[i] == alphabet[j]:
                height = h[j]
                if height > max_height:
                    max_height = height
                break

    # area = tallest letter height * number of letters
    return max_height * len(word)
# Example usage (no __main__)
h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
word = "zaba"
print(designerPdfViewer(h, word))  # Output: 28
