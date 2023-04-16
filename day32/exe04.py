"""
4. Tìm phần tử có tần suất xuất hiện nhiều nhất trong mảng và xuất hiện bao nhiêu lần
Đề bài: Nhập vào số phần tử và giá trị từng phần tử của mảng. Tìm phần tử có tần suất xuất hiện nhiều nhất trong mảng và xuất hiện bao nhiêu lần, sau đó in ra màn hình
"""

import array

nums = array.array('d', [])

n = int(input('Nhap vao so luong phan tu: '))

for i in range(n):
    num = float(input(f'Nhap vao so thuc thu {i+1}: '))
    nums.append(num)

counter = {}

for x in nums:
    if x in counter:
        counter[x] += 1
    else:
        counter[x] = 1

m = max(counter.values())

for k, v in counter.items():
    if v == m:
        print(k, 'xuat hien', v, 'lan')
