import random

"""
3 = 3 * 1
6 = 3 * 2
9 = 3 * 3 = 3^2
24 = 3 * 2 * 2 * 2 = 3 * 2^3
3^2 x 2^3 x 1^1 = 72
"""
import time

start_time = time.perf_counter()
lst = [10, 20, 3, -6, 8, 9, 123, 10, 20, 3, -6, 8, 9, 123, 10, 20, 3, -6, 8, 9, 123, 10, 20, 3, -6, 8, 9, 123]

def lcm(a, b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    m = a if a > b else b
    while True:
        if m % a == 0 and m % b == 0:
            low = m
            break
        m += 1
    return low


if len(lst) < 2:
    print("do nothing")
else:
    bcnn = lcm(lst[0], lst[1])
    for i in range(2, len(lst)):
        bcnn = lcm(bcnn, lst[i])
    print(bcnn)

end_time = time.perf_counter()
# f - fast
print(f"{end_time - start_time}s")
