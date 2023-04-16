# recursion - đệ quy
# n! = n * (n-1) * ... * 3 * 2 * 1 = n * (n-1)!
# if n=1 => 1
# else n*(n-1)!
def fac(n):
    if n == 1:
        return 1
    return n * fac(n-1)


print(fac(3)) # 6
