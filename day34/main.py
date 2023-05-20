def is_power_of_4(n):
    if n == 0:
        return False

    # 16 = 4 * 4 * 1 = 4^2
    # 4 = 4 * 1 = 4^1
    # 64 = 4 * 4 * 4 * 1 = 4^3
    # 24 = 4 * 6

    while n != 1:
        if n % 4 != 0:
            return False
        n = n // 4

    return True


print(is_power_of_4(20)) # True

# def is_prime(n):
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


# n = int(input())
# print(is_prime(n))

s1 = input()
s2 = input()

f1 = s1[:2]
f2 = s2[:2]
s1 = s1.replace(f1, f2)
s2 = s2.replace(f2, f1)

print(s1 + ' ' + s2)
