"""
input: nhập vào một năm bất kỳ
output: kiểm tra năm nhuận
"""
year = int(input("Nhap nam vao day: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("nam nhuan")
else:
    print("nam thuong")
