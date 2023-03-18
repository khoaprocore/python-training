"""
ucln(3, 6) = 3
"""
import math

a = -12
b = -18

if a < 0:
    a = -a

if b < 0:
    b = -b

# ucln
# 1
m = a if a > b else b

for i in range(m, 0, -1):
    if a % i == 0 and b % i == 0:
        gcd = i
        break

print(gcd)
print(math.gcd(-12, 18, 36, 13))
