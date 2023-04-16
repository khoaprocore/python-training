"""
1. Tính tổng, tích và giá trị trung bình của một mảng
Đề bài: Nhập vào số lượng phần tử và giá trị từng phần tử của mảng. In ra màn hình tổng, tích và giá trị trung bình của mảng đó.
"""
import array

nums = array.array('d', [])

n = int(input('Nhap vao so luong phan tu: '))

for i in range(n):
    num = float(input(f'Nhap vao so thuc thu {i+1}: '))
    nums.append(num)

tong = 0
tich = 1

for x in nums:
    tong += x
    tich *= x

print("Tong cac phan tu trong mang:", tong)
print("Tich cac phan tu trong mang:", tich)
print("TB cac phan tu trong mang:", tong / n)

