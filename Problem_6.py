"""
The sum of the squares of the first ten natural numbers is 385.
The square of the sum of the first ten natural numbers is 3025.
Hence the difference between the sum of those squares and the 
square of those sums is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
"""

# Get the square of the sum. 
s = 0
for i in range(1,101):
    s += i
squareOfSum = s**2


# Get the sum of the squares
s = 0
for i in range(1,101):
    s += i**2
sumOfSquares = s 

solution = squareOfSum - sumOfSquares
print(solution)


