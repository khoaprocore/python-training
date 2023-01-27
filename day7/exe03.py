"""
1. Tạo ra một số ngẫu nhiên trong đoạn [1, 100]
2. Nhập vào số mình chọn
3. Nếu số chọn > số ngẫu nhiên thì in ra lớn hơn ngược lại in ra nhỏ hơn
4. Nếu đúng thì dừng
"""

import random

so_ngau_nhien = random.randint(1, 100)
so_chon = int(input("Nhap so ngau nhien tu 1 den 100: "))
while True:
    if so_chon > so_ngau_nhien:
        print("lon hon")
    elif so_chon < so_ngau_nhien:
        print("nho hon")
    else:
        print("Victory")
        break
    so_chon = int(input("Nhap so ngau nhien tu 1 den 100: "))
