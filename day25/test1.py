def decrypt(s, n):
    if len(s) == 0 or n <= 0:
        return s

    ans = [0] * len(s)
    while n > 0:
        j = 0
        for i in range(1, len(ans), 2):
            ans[i] = s[j]
            j += 1
        for i in range(0, len(ans), 2):
            ans[i] = s[j]
            j += 1
        s = ''.join(ans)
        n -= 1
    return s


print(decrypt("s eT ashi tist!", 2) == "This is a test!")