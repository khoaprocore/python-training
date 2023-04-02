""" # n! = 1 x 2 x 3 x ... x n
# n! = (n-1)! x n
# 1! = 1
def factorial(n): # n = 3 => 3! = 3 x 2 x 1 = 6
    if n < 2:
        return 1
    return n * factorial(n - 1)


print(factorial(3)) # 6 """


def duplicate_count(text):
    """ text = text.lower()
    count = 0
    s = set(text)
    for x in s:
        if text.count(x) > 1:
            count += 1

    return count """

    seen, dups = set(), set()
    text = text.lower()
    for char in text:
        if char in seen:
            dups.add(char)
        seen.add(char)

    return len(dups)


print(duplicate_count("aaaabBcde"))
# sort - 20000
