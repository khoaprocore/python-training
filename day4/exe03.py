"""
input: Nhập vào hai số a, b
output: số lớn nhất và nhỏ nhất trong hai số
"""
a = float(input("Nhap vao so thuc thay a: "))
b = float(input("Nhap vao so thuc thay b: "))
if a > b:
    print("a la so lon, b la so nho")
elif a < b:
    print("b la so lon, a la so nho")
else:
    print("b va a = nhau")
