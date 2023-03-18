#      0  1  2  3  4  5  6
lst = [1, 2, 3, 4, 3, 2, 1] # 3
"""
left - 1 2 3 = 6
right - 3 2 1 = 6
left = right => 3
"""

for i in range(len(lst)):
    left = sum(lst[:i])
    right = sum(lst[i+1:])

    if left == right:
        print(i)
        break



