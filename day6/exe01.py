"""
Định nghĩa một hàm để cộng/trừ/nhân/chia hai số và gọi nó
"""


def add(n1, n2):
    return n1 + n2


# a function call
total = add(10, 29)
print(total)


def minus(x1, x2):
    return x1 - x2


subtraction = minus(9, 23)
print(subtraction)


def multiply(a, b):
    return a * b


multiple = multiply(8, 2)
print(multiple)


def divide(m, v):
    if v == 0:
        return "division by zero"
    return m / v  # float


a = b = 10
division = divide(a, b)
print(division)
