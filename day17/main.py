"""
s = "bitcoin take over the world maybe who knows perhaps"

# 1
words = s.split() # split by space+, \t, \n - newline

print(words)

_min = words[0]

for w in words:
    if len(_min) > len(w):
        _min = w

print(len(_min))

n = 92
tmp = n
p = 1

lst = []
s = 0

while n > 0:
    last = n % 10
    lst.append(last)
    n //= 10

for i in range(len(lst) - 1, -1, -1):
    s += lst[i] ** p
    p += 1

res = s / tmp

if res != int(res):
    print(-1)
else:
    print(res)
"""

s = "is2 Thi1s T4est 3a"

def get_digit(word):
    # 1abc
    for char in word:
        if char.isdigit():
            return char

words = s.split()

words.sort(key=lambda word: get_digit(word))

print(words)
