"""
+ values
+ data types
+ variables
+ built in function
"""
# values
# numbers: 1.25, 1, 3, -3
# strings: 'hello', "Dang Khoa", '''world''', """world"""
# booleans: True/False
print(1.25)
print(1)
print(.5)  # 0.5

print('Dang Khoa')
print('''
This is a cat!
''')

print(True)
print(False)

print('*' * 20)

# data types
# 1 - số nguyên - integer - int
# 1.25 - số thực - float
# type(value) => data type
print(type(1))
print(type(1.25))

print(type("Dang Khoa"))  # string - str

# variables - biến
# a name for a value
x = 5
print(x)  # 5

x = "Dang Khoa"  # str
print(x)

# x = 5
# Cmd + /
# x = x + 100  # int
# print(x)  # str + int

# Quy tắc đặt tên biến
"""
+ không được để số ở đầu tên biến
+ không được để những ký tự đặc biệt trong tên biến: !@#$%^&*()_+{}|\/
+ đặt tên biến theo chuẩn tiếng anh - a b c xyz (shouldn't)
+ tên biến in thường
"""
# 1a = 4
# $name = "Dang Khoa"
age = 23
print(age + 5)

full_name = "Bui Tran Dang Khoa"  # _ - underscore
print(full_name)
print(type(full_name))

# +, -, *, /, //, **, %
print(1 + 2)
print(-3 - 100)
print(1.25 * 2)
# print(1 / 0) - Error
print(1 / 3)  # / => float
print(1 // 3)  # // => int
print(2 ** 3)  # 8
print(1 % 3)  # 1
print(13 % 6)  # 1

# >, <, >=, <=, ==, != => True/False
print(5 > 2)  # True
print(3.0 >= 3)  # True
print('a' == 'b')  # False

print('a' == 'a')  # True

# and or not
# not > and > or
print(5 > 2 and 1 > 3)  # True and False = False | CMD + D
print(5 > 2 or 1 > 3)  # True
print(not True)  # False
print(not False)  # True

"""
and trả về giá trị bên trái khi nó được đánh giá là False
else trả về giá trị bên phải
or trả về giá trị bên trái khi nó được đánh giá là True
else trả về giá trị bên phải
not => reverse True/False
falsy: bool(value) = False
0, 0.0, 0j, '', None, False
"""
print('-' * 50)

# print(bool(''))  # True
print('' and 2)  # 0
print(1 or 2)  # 1
print(None or '')  # ''
print(not 1)  # False
print(not '')  # True

# +=, -=, *=, ...
x = 100
x += 5  # x = x + 5
print(x)

x -= 10
print(x)

x *= 2
print(x)

x /= 2
print(x)

# list, tuple, set, dict
# list - danh sách
#             0         1         2      3        4
#            -5        -4        -3     -2       -1
friends = ["Khang", "Nguyên", "Hưng", "Phát", "Minh"]
print(type(friends))
print(friends[0])  # Khang
print(friends[4])
print(friends[-4])

# Số lượng
print(len(friends))  # 5 - length - chiều dài

# Thêm một giá trị vào cuối của friends
friends.append("Bob")
print(friends)
friends.append("Anna")
print(friends)

# Xóa một người bạn từ friends
friends.remove("Nguyên")
print(friends)

# friends.remove("Kenny") - Error
# Thêm vào một danh sách người bạn khác vào cuối của danh sách ban đầu
friends.extend(["Jen", "David", "Jelly"])
print(friends)

# Lấy ra cái cuối và xóa nó đi
# pop
last = friends.pop()
print(last)
print(friends)

# Đảo ngược danh sách
friends.reverse()
print(friends)

# danh sách mới chứa 2 người bạn đầu tiên
new_friends = friends[:2]
print(new_friends)
new_friends = friends[:6]
print(new_friends)

"""
    0       1       2      3       4       5      6         7
   -8      -7       -6    -5      -4      -3      -2       -1
['David', 'Jen', 'Anna', 'Bob', 'Minh', 'Phát', 'Hưng', 'Khang']
"""
new_friends = friends[-2:]
print(new_friends)

count = friends.count("Lee")
print(count)

position = friends.index("David")
print(position)
