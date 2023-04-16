"""
Đề bài: Nhập vào kích thước và giá trị các phần tử của 2 ma trận. In ra màn hình tổng của 2 ma trận vừa nhập.
"""
# pretty print
# from pprint import pprint

n, m = [int(i) for i in input().split()]
"""
This Python function creates two matrices and subtracts them element-wise, then prints the resulting
matrix.
:return: The function `create_matrix()` is returning a 2D list (a list of lists) containing `n` rows
and `m` columns, where each element is a float value entered by the user.
"""

def create_matrix():
    arr2d = []

    for i in range(n):

        arr1d = []
        for j in range(m):
            k = float(input(f'arr2d[{i}][{j}] = '))
            arr1d.append(k)

        arr2d.append(arr1d)

    return arr2d


a1 = create_matrix()

print('-' * 20)
a2 = create_matrix()

print('-' * 20)

result = []
for x in range(n):
    tmp = []
    for y in range(m):
        tmp.append(a1[x][y] - a2[x][y])
    result.append(tmp)

for i in range(n):
    print(result[i])
