'Bài 38: Tính S(n) = CanBac N + 1(N! + CanBacN((N – 1)! + … + CanBac3(2! + CanBac2(1!))) có n dấu căn'

# n = int(input('n ='))

# S = P = 1

# for i in range(2,n+1):
#     P *= i
#     S = pow(S + P, 1/(i+1))

# print(S)

'Bài 39: Tính S(n) = CanBac2(x^n + CanBac2(x^n-1 + … + CanBac2(x^2 + CanBac2(x)))) có n dấu căn'

# n = int(input('n = '))
# x = float(input('x = '))

# S = x ** 0.5

# for i in range(2,n+1):
#     S = pow(S + x ** i, 1/(i+1))

# print(S)

'Bài 40: Tính S(n) = 1 / (1 + 1 / ( 1 + 1 / (…. 1 + 1 / 1 + 1))) có n dấu phân số'

# n = int(input('n = '))
# S = 0.5

# for i in range(1,n):
#     S = 1/(1+S)

# print(S)

'Bài 41: Cho n là số nguyên dương. Hãy tìm giá trị nguyên dương k lớn nhất sao cho S(k)  < n. Trong đó chuỗi k được định nghĩa như sau: S(k) = 1 + 2 + 3 + … + k'

# n = int(input('n = '))

# S = 0
# k = 0

# while S < n:
#     k += 1
#     S += k

# print(k - 1)

'Bài 42: Hãy đếm số lượng chữ số của số nguyên dương n'

# n = int(input('n = '))

# count = 0
# while n > 0:
#     n // 10
#     count += 1

# print(count)

'Bài 43: Hãy tính tổng các chữ số của số nguyên dương n'

# n = int(input('n = '))
# s = 0

# while n > 0:
#     s += n % 10
#     n //= 10

# print(s)

'Bài 45: Hãy tính tích các chữ số của số nguyên dương n'

# n = int(input('n = '))
# t = 1

# while n > 0:
#     t *= n % 10
#     n //= 10

# print(t)

'Bài 46: Hãy đếm số lượng chữ số lẻ của số nguyên dương n'
# 1234 => 2
# n = int(input('n = '))

# count = 0
# while n > 0:
#     r = n % 10

#     if r % 2 == 1:
#         count += 1

#     n //= 10

# print(count)


'Bài 47: Hãy tính tổng các chữ số chẵn của số nguyên dương n'

# n = int(input('n = '))

# s = 0
# while n > 0:
#     r = n % 10

#     if r % 2 == 0:
#         s += r

#     n //= 10

# print(s)

'Bài 48: Hãy tính tích các chữ số lẻ của số nguyên dương n'

# n = int(input('n = '))

# t = 1
# while n > 0:
#     r = n % 10

#     if r % 2 == 1:
#         t *= r

#     n //= 10

# print(t)

'Bài 49: Cho số nguyên dương n. Hãy tìm chữ số đầu tiên của n'

# n = int(input('n = '))

# while n > 9:
#     n //= 10

# print(n)

'Bài 50: Hãy tìm số đảo ngược của số nguyên dương n'

# import math

# n = int(input('n = '))

# l = math.floor(math.log10(n) + 1) - 1
# s = 0

# while n > 0:
#     r = n % 10
#     s += r * 10 ** l
#     n //= 10
#     l -= 1

# print(s)

'Bài 51: Tìm chữ số lớn nhất của số nguyên dương n'

# n = int(input('n = '))
# m = n % 10

# while n > 0:
#     r = n % 10

#     if m < r:
#         m = r

#     n //= 10

# print(m)

'Bài 52: Tìm chữ số nhỏ nhất của số nguyên dương n'

# n = int(input('n = '))

# m = n % 10

# while n > 0:
#     r = n % 10

#     if m > r:
#         m = r

#     n //= 10

# print(m)

'Bài 53: Hãy đếm số lượng chữ số lớn nhất của số nguyên dương n'

# n = int(input('n = '))
# y = n

# m = 0

# while n > 0:
#     r = n % 10

#     if m < r:
#         m = r

#     n //= 10

# c = 0

# while y > 0:
#     if y % 10 == m:
#         c += 1
#     y //= 10

# print(c)

'Bài 54: Hãy đếm số lượng chữ số nhỏ nhất của số nguyên dương n'

# n = int(input('n = '))
# y = n

# m = 9

# while n > 0:
#     r = n % 10

#     if m > r:
#         m = r

#     n //= 10

# c = 0

# while y > 0:
#     if y % 10 == m:
#         c += 1
#     y //= 10

# print(c)

'Bài 56: Hãy kiểm tra số nguyên dương n có toàn chữ số lẻ hay không'

# n = int(input('n = '))
# c = True
# while n > 0:
#     r = n % 10

#     if r % 2 == 0:
#         c = False
#         break

#     n //= 10

# print(c)

'Bài 57: Hãy kiểm tra số nguyên dương n có toàn chữ số chẵn hay không'

# n = int(input('n = '))
# c = True
# while n > 0:
#     r = n % 10

#     if r % 2 == 1:
#         c = False
#         break

#     n //= 10

# print(c)

'Bài 59: Hãy kiểm tra số nguyên dương n có phải là số đối xứng hay không'

# import math

# n = int(input('n = '))
# y = n

# l = math.floor(math.log10(n) + 1) - 1
# s = 0

# while n > 0:
#     r = n % 10
#     s += r * 10 ** l
#     n //= 10
#     l -= 1

# print(s == y)

'Bài 60: Hãy kiểm tra các chữ số của số nguyên dương n có tăng dần từ trái sang phải hay không'

# n = int(input('n = '))
# last = n % 10
# n //= 10

# while n > 0:
#     prev = n % 10

#     if last < prev:
#         print("khong tang")
#         break

#     last = prev
#     n //= 10

# else:
#     print("day tang")


'Bài 61: Hãy kiểm tra các chữ số của số nguyên dương n có giảm dần từ trái sang phải hay không'

# n = int(input('n = '))
# last = n % 10
# n //= 10

# while n > 0:
#     prev = n % 10

#     if last > prev:
#         print("khong giam")
#         break

#     last = prev
#     n //= 10

# else:
#     print("day giam")
