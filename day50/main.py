'Bài 159: Cho mảng 1 chiều các số thực, hãy tìm giá trị đầu tiên lớn hơn giá trị 2003. Nếu mảng không có giá trị thỏa điều kiện trên thì trả về  -1'

# n = map(float,input().split())

# for x in n:
#     if x - 2003 > 2003:
#         print(x)
#         break
# else:
#     print(-1)

'Bài 160: Cho mảng 1 chiều các số thực, hãy tìm giá trị âm cuối cùng lớn hơn giá trị -1. Nếu mảng không có giá trị thỏa điều kiện trên thì trả về -1'

# n = map(float, input('> ').split())

# i = len(n) - 1

# while i > -1:
#     if n[i] > 0 and n[i] < -1:
#         print(n[i])
#         break
#     i -= 1
# else:
#     print(-1)

'Bài 161: Cho mảng 1 chiều các số nguyên, hãy tìm giá trị đầu tiên nằm trong khoảng [x, y] cho trước. Nếu mảng không có giá trị thỏa điều kiện trên thì trả về -1'

# n = list(map(float, input('> ').split()))
# x, y = map(float, input('> ').split())

# while x > y:
#     x, y = map(float, input('> ').split())

# for i in n:
#     if x <= i <= y:
#         print(n)
#         break
# else:
#     print(-1)

'Bài 162: Cho mảng 1 chiều các số thực. Hãy viết hàm tìm một vị trí trong mảng thỏa 2 điều kiện: có 2 giá trị lân cận và giá trị tại đó bằng tích 2 giá trị lân cận. Nếu mảng không tồn tại giá trị như vậy thì trả về giá trị -1'
# n = list(map(float, input('> ').split()))

# def find_position(n):
#     for i in range(1, len(n)-1):
#         if n[i - 1] * n[i + 1] == n[i]:
#             return i
#     return -1

# print(find_position(n))

'Bài 163: Tìm số chính phương đầu tiên trong mảng 1 chiều các số nguyên'

# n = list(map(float, input('> ').split()))

# def find_square(n):
#     for i in n:
#         if (i ** 0.5).is_integer():
#             return i
#     return -1

# print(find_square(n))

'Bài 164: Cho mảng 1 chiều các số nguyên. Hãy tìm giá trị đầu tiên thỏa mãn tính chất số gánh'

# n = list(map(int, input('> ').split()))

# def find_sg(n):
#     x = 0
#     y = n
#     if n > 99:
#         while y > 0:
#             x = x * 10 + y % 10
#             y //= 10
        
#         return x == n
#     return False

# def find(n):
#     for i in n:
#         if find_sg(i):
#             return i
#     return -1

# print(find(n))

'Bài 165: Cho mảng 1 chiều các số nguyên. Hãy tìm giá trị đầu tiên có chữ số đầu tiên là chữ số lẻ'
# import math

# n = list(map(int, input('> ').split()))

# def find_f(n):
#     n = abs(n)
#     return n // 10 ** math.floor(math.log10(n))

# def find(n):
#     for i in n:
#         if find_f(i) % 2 == 1:
#             return i
#     return -1

# print(find(n))

'Bài 166: Cho mảng 1 chiều các số nguyên. Hãy viết hàm tìm giá trị đầu tiên trong mảng có'

# import math

# n = list(map(int, input('> ').split()))

# def find(n):
#     for i in n:
#         if math.log2(i).is_integer():
#             return i
#     return 0

# print(find(n))

'Bài 167: Hãy tìm giá trị thỏa điều kiện toàn chữ số lẻ và là giá trị lớn nhất thỏa điều kiện ấy trong mảng 1 chiều các số nguyên. Nếu mảng không có giá trị thỏa điều kiện trên thì trả về 0'

# n = list(map(int, input('> ').split()))

# def check_all_odds(n):
#     while n > 0:
#         l = n % 10

#         if l % 2 == 0:
#             return False
        
#         n //= 10
        
#     return True

# def f_o(n):
#     for i in n:
#         if check_all_odds(i):
#             return i
#     return -1

# def find(n):
#     f = f_o(n)

#     if f == -1:
#         return 0
    
#     for i in n:
#         if check_all_odds(i) and f < i:
#             f = i
    
#     return f

# print(find(n))

'Bài 168: Cho mảng 1 chiều các số nguyên. Hãy viết hàm tìm giá trị lớn nhất trong mảng có dạng 5^k. Nếu mảng khong tồn tại giá trị 5^k thì hàm sẽ trả về 0'

# n = list(map(int, input('> ').split()))

# def check_5k(n):
#     if n == 1:
#         return True
#     if n < 1:
#         return False
    
#     while n > 1:
#         if n % 5 != 0:
#             return False
#         n /= 5
        
#     return True

# def f_o(n):
#     for i in n:
#         if check_5k(i):
#             return i
#     return -1

# def find(n):
#     f = f_o(n)

#     if f == -1:
#         return 0
    
#     for i in n:
#         if check_5k(i) and f < i:
#             f = i
    
#     return f

# print(find(n))

'Bài 169 (*): Cho mảng 1 chiều các số nguyên. Hãy viết hàm tìm số chẵn nhỏ nhất lớn hơn mọi giá trị có trong mảng'

arr = list(map(int, input().split()))

def find_even(arr):
    if max(arr) % 2 == 0:
        return max(arr) + 2
    return max(arr) + 1

print(find_even(arr))