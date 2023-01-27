lst = [100, 34, 56, -78, 22, 10, 3, 7, 9, 11]
"""
1. Tạo ra 2 lists chứa số chẵn và lẻ riêng biệt
2. lấy ra các số chia hết cho 3 trong lst
3. Lấy ra các số nằm trong đoạn [20, 30]
4. Lấy ra số nguyên tố trong lst
"""
# evens = []
# odds = []
#
# for x in lst:
#     if x % 2 == 0:
#         evens.append(x)
#     else:
#         odds.append(x)
#
# print(evens)
# print(odds)
#
# dividend_by_3 = []
#
# for x in lst:
#     if x % 3 == 0:
#         dividend_by_3.append(x)
# print(dividend_by_3)

# in_20_30 = []
#
# for x in lst:
#     if 20 <= x <= 30:
#         in_20_30.append(x)
#
# print(in_20_30)

prime_number = []

for x in lst:
    if x >= 2:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            prime_number.append(x)
print(prime_number)
