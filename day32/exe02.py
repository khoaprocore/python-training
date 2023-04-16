"""
2. Tìm giá trị lớn nhất và nhỏ nhất của mảng
Đề bài: Nhập vào số lượng phần tử và giá trị từng phần tử của mảng, in ra màn hình giá trị lớn nhất, nhỏ nhất của mảng vừa nhập.
"""
import array

nums = array.array('d', [])

n = int(input('Nhap vao so luong phan tu: '))

for i in range(n):
    num = float(input(f'Nhap vao so thuc thu {i+1}: '))
    nums.append(num)

large = small = nums[0]

for x in nums[1:]:
    if x > large:
        large = x
    if x < small:
        small = x
print('So lon nhat', large)
print('So be nhat', small)