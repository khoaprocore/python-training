def nb_year(p0, percent, aug, p):
    y = 0
    while p0 < p:
        y += 1
        ans = p0 + p0 * (percent / 100) + aug
        p0 = ans
    return y

print(nb_year(1500, 5, 100, 5000))