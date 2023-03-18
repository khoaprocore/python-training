lst = [-12, 18, 36, 6] # 1
def gcd(a,b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    m = a if a > b else b

    for i in range(m,0,-1):
        if a % i == 0 and b % i == 0:
            return i
        
if len(lst) < 2:
    print("nothing")
else:
    one_two = gcd(lst[0],lst[1])
    for i in range(2,len(lst)):
        one_two = gcd(one_two, lst[i])
    print(one_two)
