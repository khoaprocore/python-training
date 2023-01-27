"""
input: nhập vào hai số x, y
output: in ra tổng hiệu tích thương lũy thừa chia dữ của hai số x và y
"""
x = float(input('x = '))
y = float(input('y = '))

tong = x + y
hieu = x - y
tich = x * y
thuong = x / y
luy_thua = x ** y
chia_du = x % y

print(x, '+', y, '=', tong)
print(x, "-", y, "=", hieu)
print(x, "x", y, "=", tich)
print(x, ":", y, "=", thuong)
print(x, "^", y, "=", luy_thua)
print(x, "%", y, "=", chia_du)
