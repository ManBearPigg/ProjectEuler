"""
A pythagorean triplet is a set of 3 natural numbers, a < b < c, for which
a^2 + b^2 = c^2. There exists exactly one pythagorean triplet for which a + b + c
= 1000. Find the product abc.
"""

sets = []
for i in range (1,1000):
    print(i)
    for j in range(i,1000):
        for k in range(j,1000):
            if i + j + k == 1000:
                sets.append([i,j,k])

for st in sets:
    if st[0]**2 + st[1]**2 == st[2]**2:
        print("solution is: ")
        print(st[0]*st[1]*st[2])
