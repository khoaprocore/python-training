lst = [
    [10, 0], 
    [3, 5], 
    [5, 8]
]

on = 0
off = 0

for e in lst:
    first = e[0]
    last = e[1]

    on += first
    off += last

print(on - off)
    
