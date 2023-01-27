"""
input: Nhập vào một số nguyên n
output: xem số đó có chia hết cho 15 hay không ?
"""
so_ng = int(input("Nhap vao 1 so nguyen: "))
if so_ng % 15 == 0:
    print(f"{so_ng} chia het cho 15")
else:
    print("{} khong chia het cho 15".format(so_ng))
