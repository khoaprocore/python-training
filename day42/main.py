'Bài 20: Liệt kê tất cả các “ước số” của số nguyên dương n'

# n = int(input('> '))
# while n <= 0:
#     n = int(input('> '))

# for i in range(1,n//2+1):
#     if n % i == 0:
#         print(i)
# print(n)


'Bài 21: Tính tổng tất cả các “ ước số” của số nguyên dương n'

# n = int(input('> '))
# while n <= 0:
#     n = int(input('> '))

# t = 0

# for i in range(1,n//2+1):
#     if n % i == 0:
#         t += i
# print(t + n)

'Bài 22:Tính tích tất cả các “ước số” của số nguyên dương n'

# n = int(input('> '))
# while n <= 0:
#     n = int(input('> '))

# t = 1

# for i in range(2,n//2+1):
#     if n % i == 0:
#         t *= i
# print(t * n)

'Bài 23: Đếm số lượng “ước số” của số nguyên dương n'

# n = int(input('> '))
# while n <= 0:
#     n = int(input('> '))

# t = 1

# for i in range(1, n//2+1):
#     if n % i == 0:
#         t += 1

# print(t)

'Bài 24: Liệt kê tất cả các “ước số lẻ” của số nguyên dương n'

# n = int(input('> '))
# while n <= 0:
#     n = int(input('> '))

# t = []

# for i in range(1, n//2+1):
#     if n % i == 0 and i % 2 != 0:
#         t.append(i)
# if n % 2 != 0:
#     t.append(n)

# print(t)

'Bài 25: Tính tổng tất cả các “ước số chẵn” của số nguyên dương n'

# n = int(input('> '))
# while n <= 0:
#     n = int(input('> '))

# t = 0

# for i in range(2, n//2+1):
#     if n % i == 0 and i % 2 == 0:
#         t += i
# if n % 2 == 0:
#     t += n

# print(t)

'Bài 26: Tính tích tất cả các “ước số lẻ” của số nguyên dương n'

# n = int(input('> '))
# while n <= 0:
#     n = int(input('> '))

# t = 1

# for i in range(2, n//2+1):
#     if n % i == 0 and i % 2 != 0:
#         t *= i
# if n % 2 != 0:
#     t *= n

# print(t)

'Bài 27: Đếm số lượng “ước số chẵn” của số nguyên dương n'

# n = int(input('> '))
# while n <= 0:
#     n = int(input('> '))

# t = 0

# for i in range(2, n//2+1):
#     if n % i == 0 and i % 2 == 0:
#         t += 1
# if n % 2 == 0:
#     t += 1

# print(t)

'Bài 28: Cho số nguyên dương n. Tính tổng các ước số nhỏ hơn chính nó'

# n = int(input('> '))
# while n <= 0:
#     n = int(input('> '))

# t = 1

# for i in range(2,n//2+1):
#     if n % i == 0:
#         t += i
# print(t)

'Bài 29: Tìm ước số lẻ lớn nhất của số nguyên dương n. Ví dụ n = 100 ước lẻ lớn nhất là 25'

# n = int(input('> '))
# while n <= 0:
#     n = int(input('> '))

# t = 0

# if n % 2 == 1:
#     print(n)
# else:
#     for i in range(n//2+1, 1, -1): 
#         if n % i == 0 and i % 2 == 1:
#             print(i)
#             break

'Bài 30: Cho số nguyên dương n. Kiểm tra xem n có phải là số hoàn thiện hay không'

# n = int(input('> '))
# while n <= 0:
#     n = int(input('> '))

# t = 1

# for i in range(2,n//2+1):
#     if n % i == 0:
#         t += i
# if t == n:
#     print(f'{n} là số hoàn thiện')
# else:
#     print(f'{n} là số không hoàn thiện')

'Bài 31: Cho số nguyên dương n. Kiểm tra xem n có phải là số nguyên tố hay không'

# n = int(input('> '))
# while n <= 0:
#     n = int(input('> '))

# if n < 2 :
#     print(f'{n} không phải số nguyên tố')
# else:
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             print(f'{n} không phải số nguyên tố')
#             break
#     else:
#         print(f'{n} là số nguyên tố')

'Bài 32: Cho số nguyên dương n. Kiểm tra xem n có phải là số chính phương hay không'

# n = int(input('> '))
# while n <= 0:
#     n = int(input('> '))

# sqrt = n ** 0.5

# if int(sqrt) == sqrt:
#     print(f'{n} là số chính phương')
# else:
#     print(f'{n} không là số chính phương')

'Bài 33: Tính S(n) = CanBac2(2+CanBac2(2+….+CanBac2(2 + CanBac2(2)))) có n dấu căn'

# n = int(input('> '))
# while n <= 0:
#     n = int(input('> '))

# s = 2 ** 0.5

# for i in range(2, n+1):
#     s = (2 + s)**0.5
# print(s)

'Bài 34: Tính S(n) = CanBac2(n+CanBac2(n - 1 + CanBac2( n - 2 + … + CanBac2(2 + CanBac2(1)  có n dấu căn'

# n = int(input('> '))
# while n <= 0:
#     n = int(input('> '))

# s = 1

# for i in range(2, n+1):
#     s = (i + s)**0.5
# print(s)

'Bài 35: Tính S(n) = CanBac2(n! + CanBac2((n-1)! +CanBac2((n - 2)! + … + CanBac2(2!) + CanBac2(1!)))) có n dấu căn'

# n = int(input('> '))
# while n <= 0:
#     n = int(input('> '))

# s = 1
# p = 1

# for i in range(2, n+1):
#     p *= i
#     s = (p + s)**0.5
# print(s)

'Bài 36: Tính S(n) = CanBac N(N + CanBac N - 1(N - 1 + … + CanBac3(3 + CanBac2(2))) có n - 1 dấu căn'

# n = int(input('> '))
# while n < 2:
#     n = int(input('> '))

# s = 2 **0.5

# for i in range(3, n+1):
#     s = (i+s)**(1/i)
# print(s)

'Bài 37: Tính S(n) = CanBac N + 1(N + CanBac N(N - 1 +…+CanBac3(2 + CanBac2(1)))) có n dấu căn'

# n = int(input('> '))
# while n < 1:
#     n = int(input('> '))

# s = 1

# for i in range(2, n+1):
#     s = (i+s)**(1/(i+1))
# print(s)