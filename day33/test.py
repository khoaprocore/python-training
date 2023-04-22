def is_prime(x):
    if x < 2:
        return False

    if x == 2:
        return True

    if x % 2 == 0:
        return False

    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return False

    return True


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def primeFactors(n):
    i = 2
    j = 0
    p = []
    while n > 1:
        while n % i == 0:
            n = n//i
            j += 1
        if j > 0:
            p.append((i, j))
        i += 1
        j = 0

    # return ''.join(f"({k}{f'**{v}' if v > 1 else ''})" for k, v in p)
    result = []

    for k, v in p:
        tmp = f"({k})"

        if v != 1:
            tmp = f"({k}**{v})"

        result.append(tmp)
        # if v > 1:
        #     result.append(f"({k}**{v})")
        # else:
        #     result.append(f"({k})")

    return ''.join(result)


print(primeFactors(n=86240))
