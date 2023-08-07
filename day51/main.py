'Bài 170: Cho mảng 1 chiều các số nguyên. Hãy viết hàm tìm số nguyên tố nhỏ nhất lớn hơn mọi giá trị có trong mảng'
# arr = list(map(int, input().split()))

# def prime(n):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
    
#     for x in range(3, int(n**0.5)+1, 2):
#         if n % x == 0:
#             return False
#     return True

# def find_prime(arr):
#     mx = max(arr)+1

#     while True:
#         if prime(mx):
#             return mx
#         mx += 1

# print(find_prime(arr))

'Bài 171: Cho mảng 1 chiều các số nguyên. Hãy viết hàm tìm ước chung lớn nhất của tất cả các phần tử trong mảng'


# def HCF(a, b):
#     a, b = abs(a), abs(b)
#     if a == 0 or b == 0:
#         return a + b
    
#     while a != b:
#         if a > b:
#             a -= b
#         if b > a:
#             b -= a
#     return a

# arr = list(map(int, input().split()))

# if len(arr) == 1:
#     print(arr[0])
# elif len(arr) == 0:
#     print('Array does not have any value')
# else:
#     GCD = HCF(arr[0], arr[1])
#     for i in range(2, len(arr)):
#         GCD = HCF(GCD, arr[i])
#     print(GCD)

'Bài 172: Cho mảng 1 chiều các số nguyên. Hãy viết hàm tìm bội chung nhỏ nhất của tất cả các phần tử trong mảng'

# arr = list(map(int, input().split()))

# def HCF(a, b):
#     a, b = abs(a), abs(b)
#     if a == 0 or b == 0:
#         return a + b
    
#     while a != b:
#         if a > b:
#             a -= b
#         if b > a:
#             b -= a
#     return a

# def LCM(a, b):
#     a, b = abs(a), abs(b)
#     return a * b / HCF(a, b)

# if len(arr) == 1:
#     print(arr[0])
# elif len(arr) == 0:
#     print('Array does not have any value')
# else:
#     L = LCM(arr[0], arr[1])
#     for i in range(2, len(arr)):
#         L = LCM(L, arr[i])
#     print(L)

'Bài 173 (*): Cho mảng 1 chiều các số nguyên. Hãy  viết hàm tìm chữ số xuất hiện ít nhất trong mảng'

# arr = input().split()
# narr = ''.join(arr)
# counter = {}
# for char in narr:
#     if char in counter:
#         counter[char] += 1
#     else:
#         counter[char] = 1
# min_value = list(counter.values())[0]
# min_key = list(counter.keys())[0]
# for key, value in counter.items():
#     if min_value > value:
#         min_key = key
#         min_value = value
# print(min_key)

'Bài 174 (*): Cho mảng số thực có nhiều hơn 2 giá trị và các giá trị trong mảng khác nhau từng đôi một. Hãy viết hàm liệt kê tất cả các cặp giá trị (a, b) trong mảng thỏa điều kiện a <= b'

# arr = random.sample(range(1, 101), k =10)

# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] <= arr[j]:
#             print((arr[i], arr[j]))

'Bài 175 (*): Cho mảng số thực có nhiều hơn 2 giá trị và các giá trị trong mảng khác nhau từng đôi một. Hãy viết hàm tìm 2 giá trị gần nhau nhất trong mảng (Lưu ý: Mảng có các giá trị khác nhau từng đôi một còn có tên là mảng phân biệt)'
# import random

# arr = random.sample(range(1, 101), k =10)

# arr.sort()

# distance = abs(arr[1]-arr[0])

# for i in range(2, len(arr)):
#     if abs(arr[i] - arr[i-1]) < distance:
#         distance = arr[i] - arr[i-1]
    
# for i in range(1, len(arr)):
#     if abs(arr[i] - arr[i-1]) == distance:
#         print((arr[i], arr[i-1]))

'Bài 176: Hãy liệt kê các số âm trong mảng 1 chiều các số thực'

# import numpy as ny

# arr = ny.random.uniform(low=-100, high=100, size= 10)

# for x in arr:
#     if x < 0:
#         print(x,end=' ')

'Bài 177: Hãy liệt kê các số trong mảng 1 chiều các số thực thuộc đoạn [x, y] cho trước'

import numpy as ny
import random as rm

# x, y = rm.uniform(1,101)

# arr = ny.random.uniform(low=-100, high=100, size= 10)

# while y <= x:
#     x, y = rm.uniform(1,101)

# for h in arr:
#     if x <= h <= y:
#         print(h, end=' ')

'Bài 178: Hãy liệt kê các số chẵn trong mảng 1 chiều các số nguyên thuộc đoạn [x, y] cho trước (x, y là các số nguyên)'

# arr = rm.sample(range(1, 101), k =10)

# x, y = rm.randint(1,101), rm.randint(1,101)

# while x > y:
#     x, y = rm.randint(1,101), rm.randint(1, 101)

# for h in arr:
#     if x <= h <= y and h % 2 == 0:
#         print(h,end=' ')

'Bài 179: Hãy liệt kê các giá trị trong mảng mà thỏa điều kiện lớn hơn giá trị tuyệt đối của giá trị đứng liền sau nó'

# arr = ny.random.uniform(low= -101, high= 101, size = 10)

# fl = 0

# for i in range(len(arr) - 1):
#     if arr[i] > abs(arr[i + 1]):
#         print(arr[i], end=' ')
#         fl = 1

# if fl == 0:
#     print('Not found')

'Bài 180: Hãy liệt kê các giá trị trong mảng mà thỏa điều kiện nhỏ hơn trị tuyệt đối của giá trị đứng liền sau nó và lớn hơn trị tuyệt đối của giá trị đứng liền trước nó'

# arr = ny.random.uniform(low= -101, high= 101, size = 10)

# fl = 0

# for i in range(1, len(arr) - 1):
#     if arr[i] < abs(arr[i + 1]) and arr[i] > abs(arr[i - 1]):
#         print(arr[i], end=' ')
#         fl = 1

# if fl == 0:
#     print('Not found')

'Bài 181: Cho mảng 1 chiều các số nguyên. Hãy viết hàm liệt kê các giá trị chẵn có ít nhất 1 lân cận cũng là giá trị chẵn'

# The code is finding and printing all even numbers in the array that have at least one adjacent even
# number. If no such numbers are found, it will print "Not found".
# arr = rm.sample(range(-101, 101), k = 10)

# fl = 0

# for i in range(1, len(arr) - 1):
#     if arr[i] % 2 == 0 and arr[i + 1] % 2 == 0 or arr[i] % 2 == 0 and arr[i - 1] % 2 == 0:
#         print(arr[i], end=' ')
#         fl = 1

# if fl == 0:
#     print('Not found')

'Bài 182: Cho mảng 1 chiều các số thực. Hãy viết hàm liệt kê tất cả các giá trị trong mảng có ít nhất 1 lận cận trái dấu với nó'

# arr = ny.random.uniform(low= -101, high= 101, size = 10)

# fl = 0

# for i in range(1, len(arr) - 1):
#     if arr[i] * arr[i + 1] or arr[i] * arr[i - 1]:
#         print(arr[i], end=' ')
#         fl = 1

# if fl == 0:
#     print('Not found')

'Bài 183: Hãy liệt kê các vị trí mà giá trị tại đó là giá trị tại đó là giá trị lớn nhất trong mảng 1 chiều các số thực'

# arr = ny.around(ny.random.uniform(low= -101, high= 101, size = 10), 5)

# m = arr.max()
# for i in range(1, len(arr) - 1):
#     if arr[i] == m:
#         print(i, end=' ')

'Bài 184: Hãy liệt kê các vị trí mà giá trị tại đó là số nguyên tố trong mảng 1 chiều các số nguyên'

def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0,5)+1, 2):
        if n % i == 0:
            return False
    return True

arr = ny.around(ny.random.uniform(low= -101, high= 101, size = 10), 5)

for i in range(len(arr)):
    if prime(arr[i]):
        print(i, end=' ')