'Bài 77: Viết chương trình tính tổng của dãy số sau: S(n) = 1 + 2 + 3 + … + n'

# n = int(input('> '))

# print(n*(n+1)//2)

'Bài 78: Liệt kê tất cả các ước số của số nguyên dương n'

# n = int(input('> '))
# res = [1]
# i = 2

# while i * i <= n:
#     if n % i == 0:
#         res.append(i)

#         if n//i != i:
#             res.append(n//i)
    
#     i += 1

# print(res)

'Bài 79: Hãy đếm số lượng chữ số của số nguyên dương n'

# import math

# n = int(input('> '))

# print(math.floor(math.log10(n)) + 1)

'Bài 80: Tính S(n) = x + x^2/1 + 2 + x^3/1 + 2 + 3 + … + x^n/1 + 2 + 3 + …. + N'

# n = int(input('> '))
# x = float(input('> '))

# s = p = 0

# for i in range(1,n+1):
#     p += i
#     s += pow(x, i) / p

# print(s)

'Bài 82: Viết chương trình tìm số lớn nhất trong 3 số thực a, b, c'

# a,b,c = map(float, input().split())

# m = a

# if m < b:
#     m = b
# if m < c:
#     m = c

# print(m)

'Bài 83: Viết chương trình nhập 2 số thực, kiểm tra xem chúng có cùng dấu hay không'

# b,c = map(float, input().split())

# if b * c > 0:
#     print('cung dau')
# else:
#     print('khac dau')

'Bài 84: Viết chương trình giải và biện luận phương trình bậc nhất ax + b = 0'

# b,c = map(float, input().split())

# if b == 0:
#     if c == 0:
#         print('vsn')
#     else:
#         print('vn')
# else:
#     if c == 0:
#         print(0)
#     elif (-c/b).is_integer():
#         print(int(-c/b))
#     else:
#         print(-c/b)

'Bài 85: Nhập vào tháng của 1 năm. Cho biết tháng thuộc quý mấy trong năm'

# n = int(input('> '))

# match n:
#     case 1|2|3:
#         print('Q1')
#     case 4|5|6:
#         print('Q2')
#     case 7|8|9:
#         print('Q3')
#     case 10|11|12:
#         print('Q4')
#     case _:
#         print('Invalid Month')

'Bài 86: Tính S(n) = 1^3 + 2^3 + … + N^3'

# n = int(input('> '))

# s = 0

# for i in range(n+1):
#     s += i ** 3

'Bài 87: Tìm số nguyên dương n nhỏ nhất sao cho 1 + 2 + … + n > 10000'

# s = n = 0

# while s < 10000:
#     n += 1
#     s += n
# print(n)

'Bài 88: Hãy sử dụng vòng lặp for để xuất tất cả các ký tự từ A đến Z'

# s = input()

# for ch in s:
#     if 'A' <= ch <= 'Z':
#         print(ch,end=' ')

'Bài 89: Viết chương trình tính tổng các giá trị lẻ nguyên dương nhỏ hơn N'

# N = int(input('> '))

# s = 0
# n = 1

# while n < N:
#     s += n
#     n += 2
# print(s)

'Bài 90: Viết chương trình tìm số nguyên dương m lớn nhất sao cho 1 + 2 + … + m < N'

# N = int(input('> '))

# s = 0
# m = 0

# while True:
#     s += m

#     if s >= N:
#         break

#     m += 1

# print(m -1)

'Bài 91: In tất cả các số nguyên dương lẻ nhỏ hơn 100'

# for i in range(1,100,2):
#     print(i,end=' ')

'Bài 92: Tìm ước số chung lớn nhất của 2 số nguyên dương'

a,b = map(int, input().split())

if a == 0 or b == 0:
    print(a + b)

else:
    a, b = a(abs), b(abs)

    while a != b:
        if a > b:
            a -= b
        elif b > a:
            b -= a
print(a)