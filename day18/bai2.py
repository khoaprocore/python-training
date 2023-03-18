"""
BCNN(a, b)
bcnn(3, 7) = 21
bcnn(3, 6) = 6
"""
import math

a = 3
b = 7

# bcnn(a, b)
# max
m = a

if b > a:
    m = b

while True:
    if m % a == 0 and m % b == 0:
        lcm = m
        break
    m += 1

print(lcm)
print(math.lcm(-12, 36))
