"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
from math import sqrt, floor


"""
Return the integer square root of a number.
"""
def isqrt(num):
    return int(floor(sqrt(num)))


"""
Return true if x is a factor of y, else return false.
"""
def isFactor(x,y):
    if y % x == 0:
        return True
    return False


"""
Return true if num is prime, else return false.
"""
def isPrime(num):
    for i in range(2, isqrt(num)+1):
        if num % i == 0:
            return False
    return True

"""
Return the cofactor of a number.
"""
def getCofactor(factor,num):
    if num % factor is not 0:
        print("Parameter 1 is not a factor of parameter 2 and therefore has no cofactor")
        return -1
    return num / factor




num = 600851475143
root = isqrt(num)
"""
Assuming that the solution would be greater than the sqrt of num:
"""
for i in range(2, root+1):
    if isFactor(i, num) and isPrime(getCofactor(i, num)):
        print(getCofactor(i, num))
"""
In case the solution is smaller than the sqrt of num (which turns out to be true):
"""
for i in range(2, root+1):
    if isFactor(i, num) and isPrime(i):
        print(i)


