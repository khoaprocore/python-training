'Bài 62: Cho 2 số nguyên dương a và b. Hãy tìm ước chung lớn nhất của 2 số này.'

# a = int(input('> '))
# b = int(input('> '))

# def HCF(a,b):
#     if a == 0 or b == 0:
#         return a+b
#     if a < 0: a = -a
#     if b < 0: b = -b

#     while a != b:
#         if a > b:
#             a -= b
#         elif b > a:
#             b -= a
#     return a
        
# print(HCF(a, b))

'Bài 63: Cho 2 số nguyên dương a và b. Hãy tìm bội chung nhỏ nhất của 2 số này'

# a = int(input('> '))
# b = int(input('> '))

# def LCM(a,b):
#     if a == 0 or b == 0:
#         return 0
#     if a < 0: a = -a
#     if b < 0: b = -b

#     c = a
#     d = b

#     while a != b:
#         if a > b:
#             a -= b
#         elif b > a:
#             b -= a
#     return (c * d) // a

# print(LCM(a, b))

'Bài 64 + 65 + 66: Giải phương trình bậc 1, 2, 4'

a,b,c = map(float, input().split())

if a == 0:
    if b == 0:
        if c == 0:
            print('vsn')
        else:
            print('vn')
    else:
        print(-c/b)
else:
    denta = b ** 2 - 4*a*c

    if denta > 0:
        x1 = (-b + denta**0.5) / (2*a)
        x2 = (-b - denta**0.5) / (2*a)
        print(x1,x2)

    elif denta == 0:
        print(-b/(2*a))
    else:
        print('vn')

'Bài 67: Tính S(x, n) = x – x^2 + x^3 + … + (-1)^n+1 * x^n'

# x = float(input('> '))
# n = int(input('> '))
# s = 0

# for i in range(1, n+1):
#     s += (-1) ** (i+1) * pow(x, i)

# print(s)

'Bài 68: Tính S(x, n) = -x^2 + x^4  + … + (-1)^n * x^2n'

# x = float(input('> '))
# n = int(input('> '))
# s = 0

# for i in range(1, n+1):
#     s += (-1) ** i * pow(x, 2*i)

# print(s)

'Bài 69: Tính S(x, n) = x – x^3 + x^5 + … + (-1)^n * x^2n+1'

# x = float(input('> '))
# n = int(input('> '))
# s = x

# for i in range(1, n+1):
#     s += (-1) ** i * pow(x, 2*i+1)

# print(s)

'Bài 70: Tính S(n) = 1 – 1/(1 + 2) + 1/(1 + 2 + 3)  + … + (-1)^n+1 * 1/(1 + 2 + 3+ … + n)'

# n = int(input('> '))
# s = 0
# p = 0

# for i in range(1, n+1):
#     p += i
#     s += (-1) ** (i + 1) * i/p

# print(s)

'Bài 71: Tính S(x, n) = -x + x^2/(1 + 2) – x^3/(1 + 2 + 3) + … + (-1)^n * x^n/(1 + 2 +… + n)'

# n = int(input('> '))
# x = float(input('> '))

# s = p = 0

# for i in range(1, n+1):
#     p += i
#     s += (-1) ** i * pow(x, i) / p

# print(s)

'Bài 72: Tính S(x, n) = – x + x^2/2! – x^3/3! + … + (-1)^n * x^n/n!'

# x = float(input('> '))
# n = int(input('> '))

# s = 0
# p = 1

# for i in range(1, n+1):
#     p *= i
#     s += (-1) ** i * pow(x, i) / p

# print(s)

'Bài 73: Tính S(x, n) = -1 + x^2/2! – x^4/4! + … + (-1)^n+1 * x^2n/(2n)!'

# x = float(input('> '))
# n = int(input('> '))

# s = -1
# p = 1

# for i in range(1, n+1):
#     m = i * 2
#     p *= m * (m-1)
#     s += (-1) ** i * pow(x, m) / p

# print(s)

'Bài 74: Tính S(x, n) = 1 – x + x^3/3! – x^5/5! + … + (-1)^n+1 * x^2n+1/(2n + 1)!'

# x = float(input('> '))
# n = int(input('> '))

# s = 1 - x
# p = 1

# for i in range(1, n+1):
#     m = i * 2 + 1
#     p *= m * (m-1)
#     s += (-1) ** (i+1) * pow(x, m) / p

# print(s)

'Bài 75: Kiểm tra số nguyên 4 byte có dạng 2^k hay không'

# import math
# x = float(input('> '))
# r = math.log2(32)

# if int(r) == r:
#     print(True)
# else:
#     print(False)

'Bài 76: Kiểm tra số nguyên 4 byte có dạng 3^k hay không'
# import math
# x = float(input('> '))
# r = math.log(x, 3)

# if int(r) == r:
#     print(True)
# else:
#     print(False)