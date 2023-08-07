'Bài 145: Tìm số hoàn thiện đầu tiên trong mảng 1 chiều số nguyên. Nếu mảng không có số hoàn thiện thì trả về  -1'

# def input_arr():
#     n = int(input('> '))
#     return list(map(int, input().split()))[:n]

# def perfect(n):
#     if n == 1:
#         return False
#     t = 1
#     i = 2
#     while i*i <= n:
#         if n % i == 0:
#             t += i
#             if n//i != i:
#                 t += n//i
#         i += 1

#     return n == t

# def f_first(lst):
#     for x in lst:
#         if perfect(x):
#             return x
#     return -1

# if __name__ == '__main__':
#     ip = input_arr()
#     first_perfect = f_first(ip)
#     print(first_perfect)

'Bài 146: Tìm giá trị âm đầu tiên trong mảng 1 chiều các số thực. Nếu mảng không có giá trị âm thì trả về -1'

# def input_arr():
#     n = int(input('> '))
#     return list(map(float, input().split()))[:n]

# def f_first(lst):
#     for x in lst:
#         if x > 0:
#             return x
#     return -1

# if __name__ == '__main__':
#     ip = input_arr()
#     first_perfect = f_first(ip)
#     print(first_perfect)

'Bài 147: Tìm số dương cuối cùng trong mảng số thực. Nếu mảng không có giá trị dương thì trả về  -1'

# def input_arr():
#     n = int(input('> '))
#     return list(map(float, input().split()))[:n]

# def f_first(arr):
#     n = len(arr) - 1

#     while n > -1:
#         if arr[n]>0:
#             return n
#         n -= 1
#     return -1

# if __name__ == '__main__':
#     ip = input_arr()
#     first_perfect = f_first(ip)
#     print(first_perfect)

'Bài 148: Tìm số nguyên tố cuối cùng trong mảng 1 chiều các số nguyên. Nếu mảng không có số nguyên tố thì trả về  -1'

# def input_arr():
#     n = int(input('> '))
#     return list(map(int, input().split()))[:n]

# def prime(n):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
    
#     for i in range(3,int(n**0.5)+1, 2):
#         if n % i == 0:
#             return False
#     return True

# def f_first(arr):
#     n = len(arr) - 1

#     while n > -1:
#         if prime(arr[n]):
#             return arr[n]
#         n -= 1
#     return -1

# if __name__ == '__main__':
#     ip = input_arr()
#     first_perfect = f_first(ip)
#     print(first_perfect)

'Bài 149: Tìm số hoàn thiện cuối cùng trong mảng 1 chiều các số nguyên. Nếu mảng không có số hoàn thiện thì trả về  -1'

# def input_arr():
#     n = int(input('> '))
#     return list(map(int, input().split()))[:n]

# def perfect(n):
#     if n == 1:
#         return False
#     t = 1
#     i = 2
#     while i*i <= n:
#         if n % i == 0:
#             t += i
#             if n//i != i:
#                 t += n//i
#         i += 1

#     return n == t

# def f_first(arr):
#     n = len(arr) - 1

#     while n > -1:
#         if perfect(arr[n]):
#             return arr[n]
#         n -= 1
#     return -14

# if __name__ == '__main__':
#     ip = input_arr()
#     first_perfect = f_first(ip)
#     print(first_perfect)

'Bài 150: Hãy tìm giá trị âm lớn nhất trong mảng 1 chiều các số thực. Nếu mảng không có giá trị âm thì trả về  -1'

# def input_arr():
#     n = int(input('> '))
#     return list(map(float, input().split()))[:n]

# def negative(arr):
#     for x in arr:
#         if x < 0:
#             return x
#     return -1



# def f_first(arr):
#     f_n = negative(arr)

#     if f_n == -1:
#         return -1
    
#     for x in arr:
#         if x < 0 and f_n < x:
#             f_n = x
    
#     return f_n

# if __name__ == '__main__':
#     ip = input_arr()
#     first_perfect = f_first(ip)
#     print(first_perfect)

'Bài 151: Hãy tìm số nguyên tố lớn nhất trong mảng 1 chiều các số nguyên. Nếu mảng không có số nguyên tố thì trả về -1'

# def input_arr():
#     n = int(input('> '))
#     return list(map(int, input().split()))[:n]

# def prime(n):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
    
#     for i in range(3,int(n**0.5)+1, 2):
#         if n % i == 0:
#             return False
#     return True

# def f_f(arr):
#     for x in arr:
#         if prime(x):
#             return x
#     return -1

# def f_first(arr):
#     m = f_f(arr)

#     if m == -1:
#         return -1
    
#     for x in arr:
#         if prime(x) and m < x:
#             m = x
    
#     return m

# if __name__ == '__main__':
#     ip = input_arr()
#     first_perfect = f_first(ip)
#     print(first_perfect)

'Bài 152: Hãy tìm số hoàn thiện nhỏ nhất trong mảng 1 chiều các số nguyên. Nếu mảng không có số hoàn thiện thì trả về -1'

# def input_arr():
#     n = int(input('> '))
#     return list(map(int, input().split()))[:n]

# def perfect(n):
#     if n == 1:
#         return False
#     t = 1
#     i = 2
#     while i*i <= n:
#         if n % i == 0:
#             t += i
#             if n//i != i:
#                 t += n//i
#         i += 1

#     return n == t

# def f_f(arr):
#     for x in arr:
#         if perfect(x):
#             return x
#     return -1

# def f_first(arr):
#     m = f_f(arr)

#     if m == -1:
#         return -1
    
#     for x in arr:
#         if perfect(x) and m > x:
#             m = x
    
#     return m

# if __name__ == '__main__':
#     ip = input_arr()
#     first_perfect = f_first(ip)
#     print(first_perfect)

'Bài 153: Hãy tìm giá trị chẵn nhỏ nhất trong mảng 1 chiều các số nguyên. Nếu mảng không có số chẵn thì trả về -1'

# def input_arr():
#     n = int(input('> '))
#     return list(map(int, input().split()))[:n]

# def even(n):
#     return n % 2 == 0

# def f_f(arr):
#     for x in arr:
#         if even(x):
#             return x
#     return -1

# def f_first(arr):
#     m = f_f(arr)

#     if m == -1:
#         return -1
    
#     for x in arr:
#         if even(x) and m > x:
#             m = x
    
#     return m

# if __name__ == '__main__':
#     ip = input_arr()
#     first_perfect = f_first(ip)
#     print(first_perfect)

'Bài 154: Hãy tìm vị trí giá trị âm nhỏ nhất trong mảng các số thực. Nếu mảng không có số âm thì trả về -1'

# def input_arr():
#     n = int(input('> '))
#     return list(map(float, input().split()))[:n]

# def negative(n):
#     return n < 0

# def f_f(arr):
#     for x in range(len(arr)):
#         if negative(arr[x]):
#             return x
#     return -1

# def f_first(arr):
#     m = f_f(arr)
#     for x in range(len(arr)):
#         if negative(arr[x]) and arr[m] > arr[x]:
#             m = x
    
#     return m

# if __name__ == '__main__':
#     ip = input_arr()
#     first_perfect = f_first(ip)
#     print(first_perfect)

'Bài 155: Hãy tìm giá trị trong mảng các số thực xa giá trị x nhất'


# n = int(input('> '))
# lst = list(map(float, input().split()))[:n]
# x = float(input('> '))

# res = lst[0]

# for i in range(1, len(lst)):
#     if abs(res - x) < abs(lst[i] - x):
#         res = lst [i]

# print(res)

'Bài 156: Hãy tìm giá trị trong mảng các số thực gần giá trị x nhất'

# n = int(input('> '))
# lst = list(map(float, input().split()))[:n]
# x = float(input('> '))

# res = lst[0]

# for i in range(1, len(lst)):
#     if abs(res - x) > abs(lst[i] - x):
#         res = lst [i]

# print(res)

'Bài 157: Cho mảng 1 chiều các số thực, hãy tìm đoạn [a, b] sao cho đoạn này chứa tất cả các giá trị trong mảng'

# n = int(input('> '))
# lst = list(map(float, input().split()))[:n]

# mx = mn = lst[0]

# for x in lst:
#     if mn > x:
#         mn = x
#     if mx < x:
#         mx = x

# print(mn, mx)

'Bài 158: Cho mảng 1 chiều các số thực, hãy tìm giá trị x sao cho đoạn [-x, x] chứa tất cả các giá trị trong mảng'

n = int(input('> '))
lst = list(map(float, input().split()))[:n]
mx = mn = lst[0]
for x in lst:
    if mn > x:
        mn = x
    if mx < x:
        mx = x
if abs(mx) > abs(mn):
    print([-abs(mx), abs(mx)])
else:
    print([-abs(mn), abs(mn)])
