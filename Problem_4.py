"""
A palindromic number reads the same from both ways. The largest palindrome made from the product
of two 2-digit numbers is 9909 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

#--------------------------------------------------------------------
# Return the number of characters in a string.
#--------------------------------------------------------------------
def numChars(string):
    i = 0
    for char in string:
        i += 1
    return i


#--------------------------------------------------------------------
# Return True if the integer input is palindromic, else return False.
#--------------------------------------------------------------------
def intIsPalindromic(num):
    stringNum = str(num)
    while numChars(stringNum) > 1:
        if stringNum[0] == stringNum[-1]:
            stringNum = stringNum[1:-1]
        else:
            return False
    return True
    

#--------------------------------------------------------------------
# Find the largest palindrome made from the product of two 3-digit
# numbers.
#--------------------------------------------------------------------
palindromicNums = []
for i in range(999,0,-1):
    for j in range(999,0,-1):
        k = i*j
        if intIsPalindromic(k):
            palindromicNums.append(k)
palindromicNums.sort()
print(palindromicNums[-1])
