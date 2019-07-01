sum = 2
num1 = 1
num2 = 2
num3 = 3

while num3 < 4000000:
    # If new fib is even, add to sum.
    if num3 % 2 == 0:
        sum += num3
    # Generate next fib num
    num1 = num2
    num2 = num3
    num3 = num1 + num2

print(sum)
