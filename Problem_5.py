"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any
reaminder. 

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def f():
    i = 20
    divisible = True
    while divisible:
        print(i)
        for j in range(2,21):
            if i % j != 0:
                i += 1
                break
            elif j == 20:
                return i

print(f())
