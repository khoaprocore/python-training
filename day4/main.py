"""
Câu lệnh điều kiện
if-elif-else

+ debug: chạy từng dòng code
+ breakpoint: điểm dừng
"""
# Nhập vào một số nguyên (int) từ bàn phím
number = int(input("Nhap vao mot so nguyen: "))

# Kiểm tra nếu number lớn hơn 0 thì in ra số dương
if number > 0:
    print("So duong")
# Ngược lại kiểm tra number nhỏ hơn 0 thì in ra số âm
elif number < 0:
    print("So am")
# Cuối cùng thì in ra số không
else:
    print("So khong")
