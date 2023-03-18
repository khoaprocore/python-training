x = int(input())
y = int(input())
z = int(input())
n = int(input())

# 1 1 1 2
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

result = []

for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            if i + j + k != n:
                result.append([i, j, k])

print(result)
