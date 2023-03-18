"""
n = 3
[           star  space
  "  *  ", - 1 -    2
  " *** ", - 3 -    1
  "*****"  - 5 -    0
]
"""
tower = []

n = 3

for i in range(1, n+1): # 0 1 2
    star = -1 + 2*i
    space = n - i
    final = space * ' ' + star * '*' + space * ' '
    tower.append(final)

print(tower)
