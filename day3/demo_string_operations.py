# String operations => new string
s = "Hello world!"

# uppercase
new_s = s.upper()
print(type(new_s))
print(new_s)

# lowercase
new_s = s.lower()
print(type(new_s))
print(new_s)

# title
# Hello World!
new_s = s.title()
print(type(new_s))
print(new_s)

# split
lst = s.split('w')
print(type(lst))
print(lst)

# input => split
word = input("Nhap 1 cau: ")
words = word.split()

print(type(words), words)
