"""
In ra các số nguyên tố trong đoạn [20, 900]
"""
# Nested Loop
# for i in range(5):
#     for j in range(6):
#         print(i, j)

# Check prime number
# n = 12  # khong phai snt
#
# if n < 2:
#     print(n, "khong phai so nguyen to")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print(n, "khong phai so nguyen to")
#             break # thoat ra khoi vong lap chua no
#     else:
#         print(n, "la so nguyen to")

for n in range(20, 901):
    if n >= 2:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n, end=' ')

