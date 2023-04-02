# arr = [8, 2, 6, 4, 5]

# sorted_lst = sorted(arr) # Timsort
# print(sorted_lst)

# def calculate_years(p, i, t, d):
#     y = 0
#     while p < d:
#         th = p * i * t
#         lai = p * i - th
#         p += lai
#         y += 1
        
#     return y


# print(calculate_years(1000, 0.05, 0.18, 1100) == 3)
# print(calculate_years(1000,0.01625,0.18,1200) == 14)
# print(calculate_years(1000,0.05,0.18,1000) == 0)

"""
n = 1
     012345
s = "abcdef"
odd: bdf
even: ace
         012345
n = 1 => bdface
n = 2 => daebfc
"""

def encrypt(text, n):
    i = 0
    
    while i < n:
        
        odd = even = ''
        
        for c in range(len(text)):
            if c % 2 == 0:
                even += text[c]
            else:
                odd += text[c]
                
        text = odd + even
        
        i += 1
        
    return text

print(encrypt("This is a test!", 0) == "This is a test!")
print(encrypt("This is a test!", 1) == "hsi  etTi sats!")
print(encrypt("This is a test!", 2) == "s eT ashi tist!")
print(encrypt("This is a test!", 3) == " Tah itse sits!")
print(encrypt("This is a test!", 4) == "This is a test!")
print(encrypt("This is a test!", -1) == "This is a test!")
print(encrypt("This kata is very interesting!", 1) == "hskt svr neetn!Ti aai eyitrsig")
