"""
Dict: {key: value, key1: value1, key2: value2, ...}
"""
# student = {
#     "name": "Khoa",
#     "age": 12,
#     "gender": "male"
# }

# print(type(student))
# print(student["name"]) # Khoa
# print(student["gender"])
# # print(student.get("id", "HS001"))

# student["id"] = "HS001"
# print(student)

n = 35231 # [1, 3, 2, 5, 3]

lst = []

while n > 0:
    lst.append(n % 10)
    n = n // 10

print(lst)

# print(n % 10) # 1
# n = n // 10 # 3523

# print(n % 10) # 3
# n = n // 10 # 352

# print(n % 10) # 2
# n = n // 10 # 35

# print(n % 10) # 5
# n = n // 10 # 3

# print(n % 10) # 3
# n = n // 10 # 0 => stop
