'''
Making Anagrams

Given two strings s1 and s2, return the minimum number of character deletions
needed to make the two strings anagrams.

You can delete characters from either string.

Example:
s1 = "cde"
s2 = "abc"
Output = 4
Explanation:
Delete d,e from s1 → "c"
Delete a,b from s2 → "c"
Total deletions = 4
'''

def makingAnagrams(s1, s2):
    deletions = 0

    # Convert to lists so we can remove characters
    s1_list = list(s1)
    s2_list = list(s2)

    # For every character in s1, try to match with s2
    for ch in s1:
        if ch in s2_list:
            s2_list.remove(ch)   # matched → remove from s2
        else:
            deletions += 1       # no match → delete from s1 side

    # Now remaining chars in s2_list must be deleted
    deletions += len(s2_list)

    return deletions


# Example usage:
print(makingAnagrams("cde", "abc"))         # 4
print(makingAnagrams("absdjkvuahdakejfnfauhdsaavasdlkj",
                     "djfladfhiawasdkjvalskufhafablsdkashlahdfa"))  # 19
