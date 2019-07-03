"""
By listing the first six prime numbers: 2,3,5,7,11 and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?

NOTES
Use the Sieve of Eratosthenes
"""

def sieveOfEras(num):
    count = 0
    multiples = []
    for i in range(2, num+1):
        if i not in multiples:
            count = count + 1
            if count == 10001:
                return i
            for j in range(i*i,num-1,i):
                multiples.append(j)

print(sieveOfEras(100000))

                



