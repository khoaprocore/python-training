'Bài 111: Viết chương trình in ra tam giác cân có độ cao h. Tam giác cân đặc nằm giữa màn hình | Tam giác cân rỗng nằm giữa màn hình | Tam giác  vuông cân đặc | Tam giác vuông cân rỗng'

# h = int(input('> '))

# for i in range(h):
#     for _ in range(h - i +1):
#         print(end=' ')
#     print('$ ' * i)

# for i in range(h):
#     n = 2*i-1
#     s = h-i

#     for _ in range(s):
#         print(end=' ')
    
#     for _ in range(n):
#         print('$',end='')

#     print()

# for i in range(1, h+1):
#     for j in range(1, h+i):
#         if j == h-i+1 or j == h+i-1 or i == h:
#             print('$',end='')
#         else:
#             print(end=' ')
#     print()

# for i in range(1, h+1):
#     print('$' * i)

# for i in range(1, h+1):
#     for j in range(1, h+1):
#         if j == i or j == 1 or i == h:
#             print('$',end='')
#         else:
#             print(end=' ')
#     print()

'Bài 112: Viết chương trình in ra hình chữ nhật có kích thước m x n|Hình chữ nhật đặc|Hình chữ nhật rỗng'

# m = int(input('> '))
# n = int(input('> '))

# for _ in range(m):
#     for _ in range(n):
#         print('#',end=' ')
#     print()

# for i in range(m):
#     for j in range(n):
#         if i == 0 or i == m-1 or (i > 0 and i < m - 1 and (j == 0 or j == n-1)):
#             print('^',end=' ')
#         else:
#             print(end='  ')
#     print()

'Bài 115: Viết chương trình nhập họ tên, điểm toán, điểm văn của 1 học sinh. Tính điểm trung bình và xuất ra kết quả'

# name = input('quát ít do nêm> ')
# mathp = float(input('> '))
# literaturep = float(input('> '))

# def tb(a, b):
#     return (a + b) / 2

# print(name, mathp, literaturep, tb(mathp, literaturep))

'Bài 116: Viết chương trình nhập n và tính tổng S = 1 + 2 + 3 + … + n'

# n = int(input('> '))
# def s(n):
#     t = 0
#     for x in range(n+1):
#         t += x
#     return t

# print(s(n))

'Bài 117: Viết chương trình nhập n và tính tổng S(n) = x + x^2 + x^3 + … + x^n'

# x = int(input('> '))
# n = int(input('> '))

# def t(x, n):
#     s = 0
#     for i in range(1, n+1):
#         s += x ** i
#     return s

# print(t(x, n))

'Bài 119: Liệt kê tất cả các số nguyên tố nhỏ hơn n'

# n = int(input('> '))

# def is_prime(n):
#     if n == 2:
#         return True
#     if n < 2:
#         return False
#     if n % 2 == 0:
#         return False
    
#     for i in range(3, int(n ** 0.5)+1, 2):
#         if n % i == 0:
#             return False
#     return True

# def lk(n):
#     for x in range(2, n):
#         if is_prime(x):
#             print(x,end=' ')

# lk(n)
# print()

'Bài 120: Liệt kê tất cả các số chính phương nhỏ hơn n'

# n = int(input('> '))

# def is_cp(n):
#     return (n ** 0.5).is_integer()

# def lk(n):
#     for x in range(n):
#         if is_cp(x):
#             print(x,end=' ')

# lk(n)
# print()

'Bài 122: Viết hàm tìm giá trị lớn nhất trong mảng 1 chiều các số thực'

# def find_max(arr):
#     m = arr[0]
#     for i in range(1,len(arr)):
#         if m < arr[i]:
#             m = arr[i]
#     return m
# n = int(input('> '))

# lst = []

# for i in range(n):
#     k = float(input(f'Nhap so thu {i+1}:'))
#     lst.append(k)

# print(find_max(lst))

'Bài 123: Viết hàm tìm 1 vị trí mà giá trị tại vị trí đó là giá trị nhỏ nhất trong mảng 1 chiều các số nguyên'

# def find_position_min(arr):
#     vt = 0
#     for i in range(1, len(arr)):
#         if arr[vt] > arr[i]:
#             vt = i
#     return vt

# n = int(input('> '))

# lst = []

# for i in range(n):
#     k = int(input(f'Nhap so thu {i+1}:'))
#     lst.append(k)

# print(find_position_min(lst))


'Bài 124: Viết hàm kiểm tra trong mảng các số nguyên có tồn tại giá trị chẵn nhỏ hơn 2004 hay không'

# def check_even(arr):
#     for x in arr:
#         if x < 2004 and x % 2 == 0:
#             return True
#     return False

# n = int(input('> '))

# lst = []

# for i in range(n):
#     k = int(input(f'Nhap so thu {i+1}:'))
#     lst.append(k)

# print(check_even(lst))

'Bài 125: Viết hàm đếm số lượng số nguyên tố nhỏ hơn 100 trong mảng'

# def is_prime(n):
#     if n == 2:
#         return True
#     if n < 2:
#         return False
#     if n % 2 == 0:
#         return False
    
#     for i in range(3, int(n ** 0.5)+1, 2):
#         if n % i == 0:
#             return False
#     return True

# def How_many_prime(arr):
#     c = 0
#     for x in arr:
#         if is_prime(x) and x < 100:
#             c += 1
#     return c


# n = int(input('> '))

# lst = []

# for i in range(n):
#     k = int(input(f'Nhap so thu {i+1}:'))
#     lst.append(k)
# print(How_many_prime(lst))

'Bài 126: Viết hàm tính tổng các giá trị âm trong mảng 1 chiều các số thực'

# def main():
#     n = int(input('> '))

#     s = 0

#     for i in range(n):
#         k = int(input(f'Nhap so thu {i+1}:'))
#         if k < 0:
#             s += k

#     print(s)

# if __name__ == '__main__':
#     main()

'Bài 127: Viết hàm sắp xếp mảng 1 chiều các số thực tăng dần'

# def main():
#     n = int(input('> '))

#     lst = []

#     for i in range(n):
#         k = float(input(f'nhap so thu {i+1}: '))
#         lst.append(k)
#     bubble_sort(lst)
#     print(lst)

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         already_sorted = True

#         for j in range(n-1-i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 already_sorted = False

#         if already_sorted:
#             break

# if __name__ == '__main__':
#     main()

'Bài 128 + 130: Viết hàm nhập, xuất mảng 1 chiều các số thực'

# def nhap_st():
#     n = int(input('n = '))

#     lst = []

#     for i in range(n):
#         k = float(input(f'nhap so thu {i+1}: '))
#         lst.append(k)
#     return lst


# def xuat_st(arr):
#     for x in arr:
#         print(x,end=' ')

# if __name__ == '__main__':
#     lst = nhap_st()
#     xuat_st(lst)

'Bài 129 + 131: Viết hàm nhập, xuất mảng 1 chiều các số nguyên'

# def nhap_st():
#     n = int(input('n = '))

#     lst = []

#     for i in range(n):
#         k = int(input(f'nhap so thu {i+1}: '))
#         lst.append(k)
#     return lst

# def xuat_st(arr):
#     for x in arr:
#         print(x,end=' ')

# if __name__ == '__main__':
#     lst = nhap_st()
#     xuat_st(lst)

'Bài 132: Viết hàm liệt kê các giá trị chẵn trong mảng 1 chiều các số nguyên'

# def nhap_st():
#     n = int(input('n = '))

#     lst = []

#     for i in range(n):
#         k = int(input(f'nhap so thu {i+1}: '))
#         lst.append(k)
#     return lst

# def xuat_st(arr):
#     for x in arr:
#         if x % 2 == 0:
#             print(x,end=' ')

# if __name__ == '__main__':
#     lst = nhap_st()
#     xuat_st(lst)

'Bài 133: Viết hàm liệt kê các vị trí mà giá trị tại đó là giá trị âm trong mảng 1 chiều các số thực'

# def nhap_st():
#     n = int(input('n = '))

#     lst = []

#     for i in range(n):
#         k = int(input(f'nhap so thu {i+1}: '))
#         lst.append(k)
#     return lst

# def xuat_st(arr):
#     for x in range(len(arr)):
#         if arr[x] < 0:
#             print(x,end=' ')

# if __name__ == '__main__':
#     lst = nhap_st()
#     xuat_st(lst)

'Bài 134: Viết hàm tìm giá trị lớn nhất trong mảng 1 chiều các số thực'

# def main():
#     n = int(input('> '))

#     lst = []

#     for i in range(n):
#         k = float(input(f'nhap so thu {i+1}: '))
#         lst.append(k)

# def nhap_st():
#     n = int(input('n = '))

#     lst = []

#     for i in range(n):
#         k = int(input(f'nhap so thu {i+1}: '))
#         lst.append(k)
#     return lst

# def f_max(arr):
#     m = arr[0]
#     for i in range(1, len(arr)):
#         if m < arr[i]:
#             m = arr[i]
#     return m
        
# if __name__ == '__main__':
#     lst = nhap_st()
#     print(f_max(lst))

'Bài 135: Viết hàm tìm giá trị dương đầu tiên trong mảng 1 chiều các số thực. Nếu mảng không có giá trị dương thì trả về -1'

# def main():
#     n = int(input('> '))

#     lst = []

#     for i in range(n):
#         k = float(input(f'nhap so thu {i+1}: '))
#         lst.append(k)

# def nhap_st():
#     n = int(input('n = '))

#     lst = []

#     for i in range(n):
#         k = int(input(f'nhap so thu {i+1}: '))
#         lst.append(k)
#     return lst

# def f_ft_d(arr):
#     for x in arr:
#         if x > 0:
#             return x
#     return -1
        
# if __name__ == '__main__':
#     lst = nhap_st()
#     print(f_ft_d(lst))

'Bài 136: Tìm số chẵn cuối cùng trong mảng 1 chiều các số nguyên. Nếu mảng không có giá trị chẵn thì trả về -1'

# def main():
#     n = int(input('> '))

#     lst = []

#     for i in range(n):
#         k = float(input(f'nhap so thu {i+1}: '))
#         lst.append(k)

# def nhap_st():
#     n = int(input('n = '))

#     lst = []

#     for i in range(n):
#         k = int(input(f'nhap so thu {i+1}: '))
#         lst.append(k)
#     return lst

# def f_l_e(arr):
#     n = len(arr)-1

#     while n > -1:
#         if arr[n] % 2 == 0:
#             return arr[n]
#         n -= 1
#     return -1
        
# if __name__ == '__main__':
#     lst = nhap_st()
#     print(f_l_e(lst))

'Bài 137: Tìm 1 vị trí mà giá trị tại vị trí đó là giá trị nhỏ nhất trong mảng 1 chiều các số thực'

# def main():
#     n = int(input('> '))

#     lst = []

#     for i in range(n):
#         k = float(input(f'nhap so thu {i+1}: '))
#         lst.append(k)

# def nhap_st():
#     n = int(input('n = '))

#     lst = []

#     for i in range(n):
#         k = int(input(f'nhap so thu {i+1}: '))
#         lst.append(k)
#     return lst

# def f_mn(arr):
#     if len(arr) == 0:
#         return -1
#     vt = 0
#     for i in range(len(arr)):
#         if arr[vt] > arr[i]:
#             vt = i
#     return vt
        
# if __name__ == '__main__':
#     lst = nhap_st()
#     print(f_mn(lst))

'Bài 138: Tìm vị trí của giá trị chẵn đầu tiên trong mảng 1 chiều các số nguyên. Nếu mảng không có giá trị chẵn thì sẽ trả về -1'

# def main():
#     n = int(input('> '))

#     lst = []

#     for i in range(n):
#         k = float(input(f'nhap so thu {i+1}: '))
#         lst.append(k)

# def nhap_st():
#     n = int(input('n = '))

#     lst = []

#     for i in range(n):
#         k = int(input(f'nhap so thu {i+1}: '))
#         lst.append(k)
#     return lst

# def f_e(arr):
#     for i in range(len(arr)):
#         if arr[i] % 2 == 0:
#             return i
#     return -1
        
# if __name__ == '__main__':
#     lst = nhap_st()
#     print(f_e(lst))

'Bài 139: Tìm vị trí số hoàn thiện cuối cùng trong mảng 1 chiều các số nguyên. Nếu mảng không có số hoàn thiện thì trả về giá trị  -1'

# def main():
#     n = int(input('> '))

#     lst = []

#     for i in range(n):
#         k = float(input(f'nhap so thu {i+1}: '))
#         lst.append(k)

# def nhap_st():
#     n = int(input('n = '))

#     lst = []

#     for i in range(n):
#         k = int(input(f'nhap so thu {i+1}: '))
#         lst.append(k)
#     return lst

# def sht(n):
#     s = 1
#     i = 2

#     while i*i<= n:
#         if n % i == 0:
#             s+=i

#             if n//i != i:
#                 s+=n//i
#         i+=1   
#     return s == n

# def f_l_sht(arr):
#     n = len(arr)-1
#     while n > -1:
#         if sht(arr[n]):
#             return n
#         n -= 1
#     return -1
        
# if __name__ == '__main__':
#     lst = nhap_st()
#     print(f_l_sht(lst))

'Bài 140: Hãy tìm giá trị dương nhỏ nhất trong mảng 1 chiều các số thực. Nếu mảng không có giá trị dương thì sẽ trả về -1'

# def main():
#     n = int(input('> '))

#     lst = []

#     for i in range(n):
#         k = float(input(f'nhap so thu {i+1}: '))
#         lst.append(k)

# def nhap_st():
#     n = int(input('n = '))

#     lst = []

#     for i in range(n):
#         k = int(input(f'nhap so thu {i+1}: '))
#         lst.append(k)
#     return lst

# def f_ft_d(arr):
#     for x in arr:
#         if x > 0:
#             return x
#     return -1

# def f_s_d(arr):
#     m = arr[0]

#     if m == -1:
#         return -1

#     for i in range(1,len(arr)):
#         if arr[i] > 0 and arr[i] < m:
#             m = arr[i]

#     return m
       
# if __name__ == '__main__':
#     lst = nhap_st()
#     print(f_s_d(lst))


'Bài 141: Hãy tìm vị trí giá trị dương nhỏ nhất trong mảng 1 chiều các số thực. Nếu mảng không có giá trị dương thì trả về  -1'

# def main():
#     n = int(input('> '))

#     lst = []

#     for i in range(n):
#         k = float(input(f'nhap so thu {i+1}: '))
#         lst.append(k)

# def nhap_st():
#     n = int(input('n = '))

#     lst = []

#     for i in range(n):
#         k = int(input(f'nhap so thu {i+1}: '))
#         lst.append(k)
#     return lst

# def f_ft_d(arr):
#     for x in len(arr):
#         if x > 0:
#             return x
#     return -1

# def f_s_d(arr):
#     m = arr[0]

#     if m == -1:
#         return -1

#     for i in range(1,len(arr)):
#         if arr[i] > 0 and arr[i] < arr[m]:
#             m = arr[i]

#     return m
       
# if __name__ == '__main__':
#     lst = nhap_st()
#     print(f_s_d(lst))


'Bài 142: Tìm giá trị nhỏ nhất trong mảng 1 chiều số thực'

# n = int(input('> '))

# lst = []

# for i in range(n):
#     k = float(input(f'nhap so thu {i+1}: '))
#     lst.append(k)

# m = lst[0]
# for i in range(1,len(lst)):
#     if lst[i] < m :
#         m = lst[i]
# print(m)

'Bài 143: Viết hàm tìm số chẵn đầu tiên trong mảng các số nguyên. Nếu mảng không có giá trị chẵn thì trả về  -1'

# n = int(input('> '))

# lst = []

# for i in range(n):
#     k = int(input(f'nhap so thu {i+1}: '))
#     lst.append(k)

# def f_ft_e(lst):
#     for x in lst:
#         if x % 2 == 0:
#             return x
        
# print(f_ft_e(lst))

'Bài 144: Tìm số nguyên tố đầu tiên trong mảng 1 chiều các số nguyên. Nếu mảng không có số nguyên tố thì trả về - 1'

n = int(input('> '))

lst = []

for i in range(n):
    k = int(input(f'nhap so thu {i+1}: '))
    lst.append(k)

def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def is_prime(lst):
    for x in lst:
        if prime(x):
            return x
    return -1
        
print(is_prime(lst))