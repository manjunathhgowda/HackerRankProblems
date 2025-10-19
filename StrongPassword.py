# """
# Strong Password

# A password is considered strong if:
# 1. It has at least 6 characters.
# 2. It contains at least one digit.
# 3. It contains at least one lowercase letter.
# 4. It contains at least one uppercase letter.
# 5. It contains at least one special character: !@#$%^&*()-+

# Given the password string, determine the minimum number of characters that must be added
# to make the password strong.

# Function Description:
# ---------------------
# minimumNumber(n, password):
# - n: integer, length of the password
# - password: string, current password
# Return: integer, minimum number of characters to add

# Example:
# ---------
# Input:
# 3
# Ab1
# Output:
# 3
# Explanation:
# Missing special character and length < 6 → need 3 more chars to reach minimum length 6.

# Input:
# 11
# #HackerRank
# Output:
# 1
# Explanation:
# Missing one digit only.
# """

# def minimumNumber(n, password):
#     numbers = "0123456789"
#     lower_case = "abcdefghijklmnopqrstuvwxyz"
#     upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     special_characters = "!@#$%^&*()-+"

#     # Flags to track missing character types
#     count_missing = 0
#     if not any(ch in numbers for ch in password):
#         count_missing += 1
#     if not any(ch in lower_case for ch in password):
#         count_missing += 1
#     if not any(ch in upper_case for ch in password):
#         count_missing += 1
#     if not any(ch in special_characters for ch in password):
#         count_missing += 1

#     # Password must be at least 6 characters long
#     return max(count_missing, 6 - n)
# # Direct sample test cases (no file I/O)
# examples = [
#     (3, "Ab1"),          # Expected output: 3
#     (11, "#HackerRank"), # Expected output: 1
#     (5, "aB1#c"),        # Expected output: 1 (needs 1 more char for length)
#     (6, "aB1#dE")        # Expected output: 0 (already strong)
# ]

# for n, pwd in examples:
#     print(minimumNumber(n, pwd))

def minimumAbsoluteDifference(arr):
    # Write your code here
    diff_lst=[]
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            diff_lst.append(abs(arr[i]-arr[j]))
    
    print(diff_lst)        
    print(min(diff_lst))

minimumAbsoluteDifference([3,-7,0])