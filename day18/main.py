"""
input:
x = 2
y = 3
---------------
output:
x = 3
y = 2
"""
x = 3000
y = 1000

"""
coc a: coca
coc b: pesi

coc a: pesi
coc b: coca

coc c: pesi
coc a: coc b = coca
coc b: coc c = pesi
"""
# temp = x
# x = y
# y = temp
x, y = y, x

print(x, y)
