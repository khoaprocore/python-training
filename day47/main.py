'Bài 104: Viết chương trình nhập ngày, tháng, năm. Tính xem ngày đó là ngày thứ bao nhiêu trong năm'

# def valid(y,m,d):
#     days = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
#         days[1] = 29

#     return 1 <= m <= 12 and 1 <= d <= days[m - 1]

# d, m, y = map(int, input().split())

# if valid(y,m,d):
#     res = d

#     for i in range(1, m):
#         match i:
#             case 4|6|9|11:
#                 res += 30

#             case 2:
#                 if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
#                     res += 29
#                 else:
#                     res += 28

#             case _:
#                 res += 31

#     print(res)

'Bài 105: Viết chương trình nhập 1 số nguyên có 2 chữ số.  Hãy in ra cách đọc của số nguyên này'

# n = int(input('> '))

# while 10 < n > 99:
#     n = int(input('> '))

# digits = ['Nguyên fai fai', 'Một', 'Hai', 'Ba', 'Bốn', 'Năm',
# 'Sáu', 'Bảy', 'Tám', 'Chín']

# chuc = n // 10
# donvi = n % 10

# if chuc == 1:
#     if donvi == 0:
#         print('Mười')
#     elif donvi == 5:
#         print('Mười Lăm')
#     else:
#         print(f'Mười {digits[donvi]}')

# elif donvi == 0:
#     print(f'{digits[chuc]} Mươi')
# elif donvi == 1:
#     print(f'{digits[chuc]} Mươi Mốt')
# elif donvi == 5:
#     print(f'{digits[chuc]} Mươi Lăm')

# else:
#     print(f'{digits[chuc]} Mươi {digits[donvi]}')

'Bài 106 Viết chương trình nhập 1 số nguyên có 3 chữ số.  Hãy in ra cách đọc của số nguyên này'

# n = int(input('> '))

# while 100 < n > 999:
#     n = int(input('> '))

# digits = ['Nguyên fai fai', 'Một', 'Hai', 'Ba', 'Bốn', 'Năm',
# 'Sáu', 'Bảy', 'Tám', 'Chín']

# tram = n // 100
# chuc = (n // 10) % 10
# donvi = n % 10

# if chuc == 0:
#     if donvi == 0:
#         print(f'{digits[tram]} Trăm')
#     else:
#         print(f'{digits[tram]} Trăm Lẻ {digits[donvi]}')
# else:
#     print(f'{digits[tram]} Trăm', end=' ')
#     if chuc == 1:
#         if donvi == 0:
#             print('Mười')
#         elif donvi == 5:
#             print('Mười Lăm')
#         else:
#             print(f'Mười {digits[donvi]}')

#     elif donvi == 0:
#         print(f'{digits[chuc]} Mươi')
#     elif donvi == 1:
#         print(f'{digits[chuc]} Mươi Mốt')
#     elif donvi == 5:
#         print(f'{digits[chuc]} Mươi Lăm')

#     else:
#         print(f'{digits[chuc]} Mươi {digits[donvi]}')

'Bài 107: Viết hàm tính S = CanBacN(x)'
# def CBN(n, x):
#     return (x ** 1/n)

# n, x = map(eval, input().split())
# print(CBN(n, x))

'Bài 108:  Viết hàm tính S = x^y'

# def SIU(x, y):
#     return x ** y

# x, y = map(eval, input().split())
# print(SIU(x, y))

'Bài 109: Viết chương trình in bảng cửu chương ra màn hình'

# for i in range(1, 11):
#     for n in range(1, 10):
#         print(f'{n} x {i} = {n * i}', end='\t')
#     print()

'Bài 110: Cần có tổng 200000 đồng từ 3 loại giấy bạc 1000 đồng, 2000 đồng, 5000 đồng. Lập chương trình để tìm ra tất cả các phương án có thể'

# for x in range(201):
#     for y in range(101):
#         for z in range(41):
#             if x * 1000 + y * 2000 + z * 3000 == 200000:
#                 print(f'{x} x 1000 + {y} x 2000 + {z} x 3000 = 200000')

'Bài 111: Viết chương trình in ra tam giác cân có độ cao h. Tam giác cân đặc nằm giữa màn hình | Tam giác cân rỗng nằm giữa màn hình | Tam giác  vuông cân đặc Tam giác  vuông cân rỗng'

# h = int(input('> '))

# for i in range(h):
#     for _ in range(h - i +1):
#         print(end=' ')
#     print('* ' * i)

'Bài 113: Lập chương trình tính sin(x) với độ chính xác 0.00001 theo công thức Sin(x) = x - x^3/3! + x^5/5! + … + (-1)^n . x^2n + 1/(2n + 1)!'

# x, y = map(eval, input().split())

# s = x
# p = 1

# for i in range(1, y+1):
#     m = 2 * i + 1
#     p *= m * (m - 1)
#     s += pow(-1, i) * pow(x, m) / p

# print(round(s, 5))
