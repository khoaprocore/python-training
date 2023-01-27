"""
input: nhập vào hai số a, b
output: tính căn bậc hai của 2a + b^3 - a^2
"""
# cmd + alt + L
a = float(input("a = "))
b = float(input("b = "))
bieu_thuc = (2 * a + b ** 3 - a ** 2) ** 0.5

# Kết quả = bieu_thuc
print("ket qua =", bieu_thuc)
