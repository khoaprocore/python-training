'Bài 93: Viết chương trình kiểm tra 1 số có phải là số nguyên tố hay không'

# def is_prime(n):
#     if n < 2:
#         return False
    
#     if n == 2:
#         return True
    
#     if n % 2 == 0:
#         return False
    
#     for i in range(3, int(n ** 0.5) + 1, 2):
#         if n % i == 0:
#             return False
        
#     return True

# num = int(input('> '))

# print(is_prime(num))

'Bài 94: Viết chương trình in ra tất cả các số lẻ nhỏ hơn 100 trừ các số 5, 7, 93'

# for x in range(1, 100, 2):
#     if x not in {5,7,93}:
#         print(x,end=' ')

'Bài 95: Viết chương trình nhập 3 số thực. Hãy thay tất cả các số âm bằng trị tuyệt đối của nó'

# a,b,c = map(float, input().split())

# if a < 0:
#     a = -a

# if b < 0:
#     b = -b

# if c < 0:
#     c = -c

# print(a,b,c)

'Bài 96: Viết chương trình nhập giá trị x sau tính giá trị của hàm số f(x) = 2x^2 + 5x + 9 khi x >= 5, f(x) = -2x^2 + 4x – 9 khi x < 5'

# x = int(input('> '))

# if x >= 5:
#     print(2 * x**2 + 5 * x + 9)
# else:
#     print(-2 * x ** 2 + 4 * x - 9)


'Bài 97: Viết chương trình nhập 3 cạnh của 1 tam giác, cho biết đó là tam giác gì'

# a,b,c = map(int, input().split())

# if a + b <= c or a + c <= b or b + c <= a:
#     print('khong phai tam giac')

# else:
#     if a == b == c:
#         print('tam giac deu')

#     elif a == b or b == c or c == a:
#         if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
#             print('tam giac vuong can')
#         else:
#             print('tam giac can')

#     elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
#         print('tam giac vuong')

#     elif a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
#         print('tam giac tu')

#     else:
#         print('tam giac nhon')

'Bài 98: Lập chương trình giải hệ: ax + by = c Dx + ey = f. Các hệ số nhập từ bàn phím'

# a,b,c,d,e,f = map(int, input().split())

'Bài 99: Viết chương trình nhập vào 3 số thực. Hãy in 3 số ấy ra màn hình theo thứ tự tang dần mà chỉ dùng tối đa 1 biến phụ'

# a,b,c = map(float, input().split())

# if a > b:
#     a, b = b, a
# if a > c:
#     a, c = c, a
# if b > c:
#     b, c = c, b

# print(a, b, c)

'Bài 101: Viết chương trình nhập tháng, năm. Hãy cho biết tháng đó có bao nhiêu ngày'

# m, y = map(int, input().split())

# if 0 < m < 13 and y > 0:
#     days = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
#         days[1] = 29

#     print(days[m - 1])

# else:
#     print('Invalid Month')

'Bài 102: Viết chương trình nhập vào 1 ngày ( ngày, tháng, năm). Tìm ngày kế ngày vừa nhập (ngày, tháng, năm)'

# d, m, y = map(int, input().split())

# def valid(y,m,d):
#     days = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
#         days[1] = 29

#     return 0 < m < 13 and 0 < d <= days[m - 1]

# def last_day(y, m):
#     days = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
#         days[1] = 29

#     return(days[m - 1])

# if valid(y,m,d):
#     if d == last_day(y, m) and m == 12:
#         d = 1
#         m = 1
#         y += 1
#     elif d == last_day(y, m):
#         d = 1
#         m += 1
#     else:
#         d += 1

#     print(d, m, y)

# else:
#     print('Invalid date')

'Bài 103: Viết chương trình nhập vào 1 ngày ( ngày, tháng, năm). Tìm ngày trước ngày vừa nhập (ngày, tháng, năm)'

# d, m, y = map(int, input().split())

# def last_day(y, m):
#     days = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
#         days[1] = 29

#     return(days[m - 1])

# def valid(y,m,d):
#     days = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
#         days[1] = 29

#     return 0 < m < 13 and 0 < d <= days[m - 1]

# if valid(y,m,d):
#     if d == 1 and m == 1:
#         d = 31
#         m = 12
#         y -= 1
#     elif d == 1:
#         d = last_day(y,m-1)
#         m -= 1
#     else:
#         d -= 1

#     print(d, m, y)

# else:
#     print('Invalid date')