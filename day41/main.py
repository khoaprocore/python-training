'Bài 1: Tính S(n) = 1 + 2 + 3 + … + n'

# n = int(input())
# s = 0

# while n != 0:
#     s += n
#     n -= 1
# print(s)

'Bài 2: Tính S(n) = 1^2 + 2^2 + … + n^2'

# s = 0
# n = int(input())

# while n != 0:
#     s += n ** 2
#     n -= 1
# print(s)

'Bài 3: Tính S(n) = 1 + ½ + 1/3 + … + 1/n'

# s = 1
# n = int(input())

# while n != 0:
#     s += 1/n
#     n -= 1
# print(s)

'Bài 4: Tính S(n) = ½ + ¼ + … + 1/2n'

# s = 0
# n = int(input())

# for i in range(1,n+1):
#     s += 1/(2*i)
# print(s)

'Bài 5: Tính S(n) = 1 + 1/3 + 1/5 + … + 1/(2n + 1)'

# s = 0 
# n = int(input())


# for i in range(1, 2*n+2, 2):
#     s += 1/i
# print(round(s, 2))

'Bài 6: Tính S(n) = 1/1×2 + 1/2×3 +…+ 1/n x (n + 1)'

# s = 0
# n = int(input())

# for i in range(1, n+1):
#     s += 1/(i*(i+1))
# print(s)

'Bài 7: Tính S(n) = ½ + 2/3 + ¾ + …. + n / n + 1'

# s = 0
# n = int(input())

# for i in range(1,n+1):
#     s += i/(i+1)
# print(s)

'Bài 8: Tính S(n) = ½ + ¾ + 5/6 + … + 2n + 1/ 2n + 2'

# s = 0
# n = int(input())

# for i in range(n+1):
#     s += (2*i+1)/(2*i+2)
# print(s)

'Bài 9: Tính T(n) = 1 x 2 x 3…x N'

# s = 1
# n = int(input())

# while n != 0:
#     s *= n
#     n -= 1
# print(s)

'Bài 10: Tính T(x, n) = x^n'

# x = float(input())
# n = int(input())

# s = 1

# for i in range(n):
#     s *= x
# print(s)

'Bài 11: Tính S(n) = 1 + 1.2 + 1.2.3 + … + 1.2.3….N'

# n = int(input("n = "))

# S = 0
# P = 1
# i = 1

# while i <= n:
#     P *= i
#     S += P
#     i += 1

# print(S)

'Bài 12: Tính S(n) = x + x^2 + x^3 + … + x^n'
# x = float(input("x = "))
# n = int(input("n = "))
# s = 0

# while n != 0:
#     s += x ** n
#     n -= 1
# print(s)

'Bài 13: Tính S(n) = x^2 + x^4 + … + x^2n'
# x = float(input("x = "))
# n = int(input("n = "))
# s = 0

# for i in range(2, 2*n+2, 2):
#     s += x**i
# print(s)

'Bài 14: Tính S(n) = x + x^3 + x^5 + … + x^2n + 1'

# x, n = map(eval, input('> ').split())
# s = 0
# for i in range(1, 2*n+2, 2):
#     s += x**i
# print(s)

'Bài 15: Tính S(n) = 1 + 1/1 + 2 + 1/ 1 + 2 + 3 + ….. + 1/ 1 + 2 + 3 + …. + N'

# n = int(input("n = "))

# S = P = 0

# for i in range(1, n+1):
#     P += i
#     S += 1/P
# print(S)

'Bài 16: Tính S(n) = x + x^2/1 + 2 + x^3/1 + 2 + 3 + … + x^n/1 + 2 + 3 + …. + N'
# x = float(input("x = "))
# n = int(input("n = "))

# P = S = 0

# for i in range(1, n+1):
#     P += i
#     S += x**i/P
# print(S)

'Bài 17: Tính S(n) = x + x^2/2! + x^3/3! + … + x^n/N!'

# x = float(input("x = "))
# n = int(input("n = "))

# P = 1
# S = 0

# for i in range(1, n+1):
#     P *= i
#     S += x**i/P
# print(S)

'Bài 18: Tính S(n) = 1 + x^2/2! + x^4/4! + … + x^2n/(2n)!'
# import math

# x = float(input("x = "))
# n = int(input("n = "))
# s = 1
# for i in range(2,2*n+1,2):
#     s += x**i/math.factorial((i))
# print(s)

'Bài 19: Tính S(n) = 1 + x + x^3/3! + x^5/5! + … + x^(2n+1)/(2n+1)!'

# x = float(input("x = "))
# n = int(input("n = "))

# s = 1 + x
# p = 1


# for i in range(1,n+1):
#     m = 2*i+1
#     p *= m*(m-1)
#     s += x**m/p
# print(s)
