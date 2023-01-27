"""
input: Nhập vào một số nguyên n
output: n là chẵn hay lẻ
"""
int_number = int(input("Nhap vao 1 so nguyen: "))  # input => str

if int_number % 2 == 0:
    print("so chan")
else:
    print("so le")
