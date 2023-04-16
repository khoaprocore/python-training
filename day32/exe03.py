"""
3. Sắp xếp mảng theo giá trị tăng dần
Đề bài: Nhập vào số phần tử và giá trị từng phần tử của mảng. Sắp xếp mảng trên và in ra màn hình kết quả theo chiều tăng dần.
"""

import array

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key_item:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key_item

    return arr

nums = array.array('d', [])

n = int(input('Nhap vao so luong phan tu: '))

for i in range(n):
    num = float(input(f'Nhap vao so thuc thu {i+1}: '))
    nums.append(num)

a = insertion_sort(nums)
print(list(a))

