"""
n = 1 => s
n != 1 => s + func(s, n-1)
"""
""" def repetition(s, n):
    if n == 1:
        return s
    return s + repetition(s, n-1)


print(repetition('kiwi', 80))
""" 

""" def search(lst, item, index=0):
    if index == len(lst):
        return -1
    
    if lst[index] == item:
        return index
    
    return search(lst, item, index+1)

print(search([1, 2, 3, 4], 3)) """

""" def sum_recursively(lst):
    if len(lst) == 0:
        return 0
    
    return lst[-1] + sum_recursively(lst[:-1])

print(sum_recursively([1, 2, 3, 4])) """

""" def add_up(num):
    if num == 0:
        return 0
    return num + add_up(num-1)

print(add_up(700)) """

import time

d1 = time.strptime("July 11, 2015", "%B %d, %Y")
d2 = time.strptime("July 9, 2015", "%B %d, %Y")

print(d1 <= d2)